from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Length


class NewCategoryForm(FlaskForm):
    category_name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    use_in_budget = BooleanField('Use in Budget')
    # cancel =
    submit = SubmitField('Submit')
