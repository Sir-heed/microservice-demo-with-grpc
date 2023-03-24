### This is a sample project that shows the implementation of microservice uisng grpc ###

The project consists of 2 applications built with Django and connected to each other using
grpc. A full explanation fo how grpc works can be found int their documentation here `https://grpc.io/`.
The same implemetation using pika and RabbitMQ can be found here ``.

The 2 Django applications are added as services on the  docker compose file which also includes services for 
their respective grpc server, hence we have 4 servers running on the applications.

The application has some dependencies which need to be stated:
- git+https://github.com/profmcdan/django-grpc-framework.git@main 
    This library is built on `djangogrpcframework` (can be found here `https://github.com/fengsp/django-grpc-framework`) 
    which has some bugs. The bugs have been fixed in this forked version but since the owner of `djangogrpcframework` has 
    not been accepting changes for some reasons, the update could not be pushed there.

- git+https://github.com/Sir-heed/micorservice-demo-with-grpc-shared-utils.git@main
    This in not a dependency perse, as it houses the generated grpc code based on the proto file created within the project, the grpc
    codes are need needed between both application, hence i packaged the folder and install them as dependencies. 
    This is uninstalled first and then installed again to relect updated changes if there are any, this is implementec in the 
    `entrypoint.sh` file.


### Project Summary ### 

The first application `dashboard` includes an API to create, update or delete a product, then the same actions are implemented on the
product table of the `product` application.

The second application `product` includes an API to like a product, then on the `dashboard` application, the number of likes of that
particular product increases by 1.


### Run the project ###

To start the project:
- Clone the repo and run docker-compose up
