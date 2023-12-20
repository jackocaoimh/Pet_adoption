from flask import Flask, render_template, Response, flash, request, redirect
from models import db, connect_db, Pet
from forms import PetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ASDF'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jackocaoimh:turner12345@localhost/adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG'] = True

db.init_app(app)
connect_db(app)  

@app.route('/')
def root():
    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():

    form = PetForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_pet = Pet(name = form.name.data,
                      species = form.species.data,
                      photo_url = form.photo_url.data,
                      age = form.age.data,
                      notes = form.notes.data)
        db.session.add(new_pet)
        db.session.commit()
        flash('New pet added successfully!', 'success')

        return redirect('/')
    
    else:
        print("Form errors:", form.errors)

    return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_pet_info(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url =  form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash('Pet updated succesfully!', 'Success')
        return redirect(f'/{pet_id}')
    
    return render_template('pet_detail.html', form=form, pet=pet)