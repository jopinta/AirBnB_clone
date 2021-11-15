![img](https://i.imgur.com/6JaLQ4z.png)
# AirBnB clone

For this project we cloned the Airbnb to hbnb. The goal was to build a full web
application. We created a partent class BaseModel in order to initialize, serial
i ze and deserialize future instances to dictionaries to JSON string back to the
file. The classes created (User, State, City, Place, Review) will inherit from t
he Super Class. Lastly was created ther storage engine (File Storage)

To do the instantiation of the objects created we use the __init__ method reciev
ing the arguments and the dictionaries(*args, **kwargs)


The attributes of the BaseMdel (,unique id-random generated with uiuid ) an
d created_at and updated_ at
The instanes attributes will be returned with __str__

Serialization and Deserializarion are made with save and reload methods respecti
vily.

The method to_dict is to generate a dictionary representation of instances after
adding the key __class__ to the dictionary.

With the console we were able to show the promt and gave some funtionality like
quit to exit with the EOF.

do_create and do_show will work with the split (shlex) cheking for the arguments
passed and depending of the index will be the name or the id.
With do_all the objects are created in a list. When called alone will return all
of them but when called with a name object will give all of this kind.

do_destroy is to eliminate one object with the id. we use the boolean because
the elemnt declared is holding the key from the JSOn  and if exists will go to t
rue anf if is in the storage will print it




summary
airbnb_ clone
we created a console to be able to create objects.
also we do some file serialization in there and lastly was created the storage e
ngine


we used HTML to give a visual interface so the user can


mysql to use different types of storage

html with fabric so we were able to put all what we did on servers

The flask web application server is where we use the models that are in storage
and to integrate them with HTML

the Rest Api works taking things that are objects and put them into JSON

Web Dynamic to take the JSON API and integrate it with the HTML in order to...



===================Video content==========================================
