from abc import ABCMeta, abstractmethod

class Director(object, metaclass = ABCMeta):
    
    def __init__(self) -> None:
        self._builder = None
    
    def set_builder(self, builder) -> None:
        self._builder = builder

    @abstractmethod
    def construct(self):
        pass

    def get_constructed_object(self):
        return self._builder.constructed_object

class FormDirector(Director):
    def __init__(self):
        Director.__init__(self)
    
    def construct(self, field_list):
        for field in field_list:
            if field["field_type"] == "text_field":
                self._builder.add_text_field(field)
            elif field["field_type"] == "checkbox":
                self._builder.add_checkbox(field)
            elif field["field_type"] == "button":
                self._builder.add_button(field)

class AbstractFormBuilder(object, metaclass = ABCMeta):

    def __init__(self,constructed_object) -> None:
        self.constructed_object = constructed_object

    @abstractmethod
    def add_text_field(self, field_dict):
        pass

    @abstractmethod
    def add_checkbox(self, field_dict):
        pass
    
    @abstractmethod
    def add_button(self, field_dict):
        pass
    
class HtmlFormBuilder(AbstractFormBuilder):
    
    def __init__(self) -> None:
        self.constructed_object = HtmlForm()

    def add_text_field(self, field_dict: list) -> None:
        self.constructed_object.field_list.append(
        f"""{field_dict['label']}:<br><input type="text" name="{field_dict['field_name']}"><br>"""
        )
    
    def add_checkbox(self, checkbox_dict):
        self.constructed_object.field_list.append(
            '<label><input type="checkbox" id="{0}" value="{1}"> {2}<br>'.
                format(
                checkbox_dict['field_id'],
                checkbox_dict['value'],
                checkbox_dict['label']
                )
            )

    def add_button(self, button_dict):
        self.constructed_object.field_list.append(
            '<button type="button">{}</button>'.format(
                button_dict['text']
                )
            )

class HtmlForm(object):
    
    def __init__(self) -> None:
        self.field_list = []
    
    def __repr__(self) -> str:
        return "<form>{}</form>".format("".join(self.field_list))
    
if __name__ == "__main__":
    director = FormDirector()
    html_form_builder = HtmlFormBuilder()
    director.set_builder(html_form_builder)
    field_list = [
        {
        "field_type": "text_field",
        "label": "Best text you have ever written",
        "field_name": "Field One"
        },
        {
        "field_type": "checkbox",
        "field_id": "check_it",
        "value": "1",
        "label": "Check for on",
        },
        {
        "field_type": "text_field",
        "label": "Another Text field",
        "field_name": "Field One"
        },
        {
        "field_type": "button",
        "text": "DONE"
        }
    ]
    director.construct(field_list)
    with open("form_file.html", 'w') as f:
        f.write(
            "<html><body>{0!r}</body></html>".format(
                director.get_constructed_object()
            )
        )