---
hide:
  - navigation
---

# Getting started

## Start Full-Stack of ExplorViz

1\. Clone the [deployment](https://github.com/ExplorViz/deployment) repo and `cd` into the correct directory.

```sh
git clone https://github.com/ExplorViz/deployment.git
cd deployment/docker/
```

2\. Use `docker compose` to start ExplorViz' software environment and its services. The frontend is served via nginx and by default runs on port `8080`. You can change ports and hostnames in the (hidden) `.env` file.

```sh
docker compose up --pull=always -d
```

3\. Open [http://localhost:8080](http://localhost:8080) in your web browser.

4\. You will see a [Software Landscape](/3-architecture) called "Default Landscape" in a table. Click on the :octicons-info-24: icon to see the [Landscape Token](/3-architecture)'s (normally auto-generated) `value` and `secret`. This pair of data is used in the upcoming instrumentation configuration. With that, every incoming data record can be mapped to a user and the software landscape which is identified by the landscape token.

## Visualize a Running Application

In this section we explore how to visualize your desired application's runtime behavior. Therefore, we employ a dynamically analyzed Java example application. For the visualization of a running application, the full software stack of ExplorViz needs to be running.

### Start the target Java application

5\. `cd` into the example applications directory. We use the [Spring PetClinic](https://github.com/spring-projects/spring-petclinic) as an example for now.

```sh
cd deployment/example-applications/petclinic-demo/
```

6\. Open the hidden `.env` file. Normally, this is the instrumentation configuration file where you would paste your token's `value` and `secret`. Since we use the default token for this instruction, you don't need that.

7\. Use `docker compose` to start the PetClinic.

```sh
docker compose up --pull=always -d
```

### Explore the runtime behavior

1\. Open [http://localhost:18080](http://localhost:18080) (frontend of PetClinic) in your web browser and generate some load by clicking around.

2\. Open [http://localhost:8080](http://localhost:8080) (frontend of ExplorViz) in your web browser and click on "Default Landscape" to open the visualization of the Spring PetClinic's runtime behavior.

3\. The visualization is updated every ten seconds and shows the aggregated runtime behavior of the Spring PetClinic.

4\. Right click (on the white background) to access the context menu.

5\. In the top corners you can find buttons to open sidebars with additional settings and features.


## Visualization Demo with Mocked Backend

Below you can find instructions that will set up a demo of ExplorViz' frontend component with exemplary data, i.e.,a mocked backend with previously recorded data from a target application.
This demo can be used to explore our visualization approach, but is not fully functional due to the mocked backend.
For the visualization demo, you can also [try out our hosted demo instance](https://demo.explorviz.uni-kiel.de):

1\. Clone the [deployment](https://github.com/ExplorViz/deployment) repo and `cd` into the directory of the frontend demo.

```sh
git clone https://github.com/ExplorViz/deployment.git
cd deployment/frontend-demo/
```

2\. Use `docker compose` to start the software stack. The frontend will run on port `8080`. You can change all ports in the (hidden) `.env` file.

```sh
docker compose up --pull=always -d
```

3\. Open [http://localhost:8080](http://localhost:8080) in your web browser (we recommend Google Chrome)

---
