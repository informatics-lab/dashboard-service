# dashboard-service
Create services to publish dynamic dashboards (v. early stages). The Jupyter Dashboard project is sadly no longer supported, so we're working on using Bokeh. Our aim is to make the publishing workflow from notebook to (public or authenticated) dashboard as easy as possible.

Early prototype, under construction

setup
prereqs: dependencies in requirements.txt. 

- cd into bokeh_apps/, run ```bokeh serve --allow-websocket-origin=* slider.py```
- cd into weather_dashboards/
- ```python manage.py migrate # set up database```
- ```python manage.py createsuperuser # create admin, whatever details you want```
- ```docker build -t dashboards . # currently copies database in so all tables need to already exist```
- ```docker run -d -p 8000:8000 dashboards```
- visit http://localhost:8000/admin/, login
- add new group and dashboard. dashboard url is from bokeh server, probably http://localhost:5006/slider
- visit http://localhost:8000/dashboards/1 :)

Setup will be smoother soon :)
