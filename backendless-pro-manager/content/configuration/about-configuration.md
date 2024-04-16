# About Backendless PRO configuration
Backendless can be configured with env variable and with Consul key value storage

Enviroment variable has hier priority then values from consul.
To setup ENV just add it as env to kubernetes workload. To ovveride value from consul use the following pattern:
`BL_PROPERTY_<key-from-consul>` for example to override key `config/application/reservedApplications` and ENV
`BL_PROPERTY_config_application_reservedApplications=20`

To access the consul you can use port 32600, so you can use http://<your-public-ip>:32600
Or you can go to Pro Manager and configure the domain with user and password: 
![img.png](./img/cunsul-domain-setup.png)
Also on this screan you can turn on port 32600, to protect access to you configuration values