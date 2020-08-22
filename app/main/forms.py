from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Length


class NewCategoryForm(FlaskForm):
    category_name = StringField('Name', validators=[DataRequired(), Length(max=50)], render_kw={'autofocus': True})
    use_in_budget = BooleanField('Use in Budget')
    cancel = SubmitField('Cancel')
    submit = SubmitField('Submit')

    def fill_from_db(self, category):
        if category is not None:
            self.category_name.data = category.name
            self.use_in_budget.data = category.use_in_budget
