from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from sqlalchemy import Enum
import arrow
from . import db




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    # users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'


class User( UserMixin, db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(50),index = True)
    email = db.Column(db.String(100),unique = True,index = True)
    password  = db.Column(db.String())
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    
    def verify_password(self,password):
        return check_password_hash(self.password,password)

    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    
    



choices = ['product', 'interview', 'promotion']
category_enum = Enum(*choices, name='category_enum')

class Pitch(db.Model):
    
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    description = db.Column(db.String(), index = True)
    title = db.Column(db.String())
    category = db.Column(category_enum, server_default='product')
    date = db.Column(db.DateTime, nullable=False, default=arrow.utcnow().datetime)
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)
    comments = db.relationship('Comment', backref='pitches', lazy='dynamic')

    def __repr__(self):
        return f'Pitch {self.description}'
    

    @classmethod
    def get_pitches(cls,owner_id):
        pitches = Pitch.query.filter_by(owner_id=owner_id).all()
        return pitches  

class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key=True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
    comment = db.Column(db.Text)
    
    def __repr__(self):
        return f"Comment('{self.user}', '{self.comment}')'"
    
    def save_comment(self):

        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_coments(cls,pitch_id):
        Comment = Comment.query.filter_by(pitch_id=pitch_id).all()
        return Comment 
        

