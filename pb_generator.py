from sqlalchemy import (create_engine, Column, Integer, String)
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from xml.dom import minidom, Node
import logging
logging.basicConfig(filename='/tftpboot/phonebook_gen.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
Base = declarative_base()

class Contacto(Base):
    __tablename__ = 'users'
    extension = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)

    def __init__(self, name, extension):
        self.name = name
	self.extension = extension

engine = db.create_engine('mysql+mysqldb://freepbxuser:2eXBJu5FhdKZ@127.0.0.1:3306/asterisk')
connection = engine.connect()
metadata = db.MetaData()
usuarios = db.Table('users', metadata, autoload=True, autoload_with=engine)

Session = sessionmaker(bind=engine)
session = Session()
listaContactos = session.query(Contacto)

contacto = session.query(Contacto).first()

doc = minidom.Document()
doc.appendChild(doc.createComment("Libreta de direcciones para telefonos Yealink"))
groupContact = doc.createElement('root_contact')
doc.appendChild(groupContact)


for c in listaContactos:
	contact = doc.createElement('contact')
	groupContact.appendChild(contact)
	
	contact.setAttribute('display_name',c.name)
        contact.setAttribute('office_number',c.extension)
        contact.setAttribute('mobile_number',"")
        contact.setAttribute('other_number', "")
        contact.setAttribute('line',"-1")
        contact.setAttribute('ring', "Auto")
        contact.setAttribute('group_id_name', "All Contacts")


archixml = open("/tftpboot/phonebook_gen.xml","wb")
doc.writexml(archixml,'\n')
archixml.close()
logging.info('PhoneBook generada correctamente.')
