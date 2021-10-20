#Reference from Corey Schafer Youtube
from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, validators, SubmitField


class InputForm(FlaskForm):
    workclass = [' State-gov', ' Self-emp-not-inc', ' Private', ' Federal-gov', ' Local-gov', ' Self-emp-inc',
                 ' Without-pay']
    education = [' Bachelors', ' HS-grad', ' 11th', ' Masters', ' 9th', ' Some-college', ' Assoc-acdm', ' 7th-8th',
                 ' Doctorate', ' Assoc-voc', ' Prof-school', ' 5th-6th', ' 10th', ' Preschool', ' 12th', ' 1st-4th']
    martial_status = [' Never-married', ' Married-civ-spouse', ' Divorced', ' Married-spouse-absent', ' Separated',
                      ' Married-AF-spouse', ' Widowed']
    occupation = [' Adm-clerical', ' Exec-managerial', ' Handlers-cleaners', ' Prof-specialty', ' Other-service',
                  ' Sales', ' Transport-moving', ' Farming-fishing', ' Machine-op-inspct', ' Tech-support',
                  ' Craft-repair', ' Protective-serv', ' Armed-Forces', ' Priv-house-serv']
    relationship = [' Not-in-family', ' Husband', ' Wife', ' Own-child', ' Unmarried', ' Other-relative']
    race = [' White', ' Black' ,' Asian-Pac-Islander', ' Amer-Indian-Eskimo' ,' Other']
    sex = ['Male', 'Female']
    country = [' United-States', ' Cuba', ' Jamaica', ' India', ' Mexico', ' Puerto-Rico', ' Honduras', ' England',
               ' Canada', ' Germany', ' Iran', ' Philippines', ' Poland', ' Columbia', ' Cambodia', ' Thailand',
               ' Ecuador', ' Laos', ' Taiwan', ' Haiti', ' Portugal', ' Dominican-Republic', ' El-Salvador', ' France',
               ' Guatemala', ' Italy', ' China', ' South', ' Japan', ' Yugoslavia', ' Peru',
               ' Outlying-US(Guam-USVI-etc)',
               ' Scotland', ' Trinadad&Tobago', ' Greece', ' Nicaragua', ' Vietnam', ' Hong', ' Ireland', ' Hungary',
               ' Holand-Netherlands']

    Age = IntegerField("Age", validators=[validators.DataRequired()])
    Hours_Per_Week = IntegerField("Hours Per Week", validators=[validators.DataRequired()])
    Final_Weight = IntegerField("Final Weight", validators=[validators.DataRequired()])
    Workclass = SelectField("Workclass", choices=workclass)
    Education = SelectField("Education", choices=education)
    Martial_Status = SelectField("Martial Status", choices=martial_status)
    Occupation = SelectField("Occupation", choices=occupation)
    Relationship = SelectField("Relationship", choices=relationship)
    Race = SelectField("Race", choices=race)
    Sex = SelectField("Sex", choices=sex)
    Country = SelectField("Country", choices=country)

    submit = SubmitField("Predict")
