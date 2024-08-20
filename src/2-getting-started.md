---
hide:
  - navigation
---

# Getting started

## Quick start

Below you can find instructions that will set up a demo of ExplorViz' frontend component with exemplary data, i.e., mocked backend and target application. You can also [try out our hosted demo instance](https://samoa.se.informatik.uni-kiel.de):

1\. Clone the [deployment](https://github.com/ExplorViz/deployment) repo and `cd` into the directory of the frontend demo.

```sh
git clone https://github.com/ExplorViz/deployment.git
cd deployment/frontend-demo/
```

2\. Use `docker compose` to start the software stack. The frontend will run on port `8080`. You can change all ports in the (hidden) `.env` file.

```sh
docker compose up --pull=always -d
```

3\. Open [http://localhost:8080](http://localhost:8080) in your web browser, e.g. Mozilla Firefox.

---

## Visualize a Java application

Instead of using the approach that is shown above, you can also start the complete software stack of ExplorViz to visualize and explore your desired Java application's runtime behavior. Below you can find instructions that will set up ExplorViz' complete software stack with a dynamically analyzed example application.

### Start ExplorViz

1\. Clone the [deployment](https://github.com/ExplorViz/deployment) repo and `cd` into the correct directory.

```sh
git clone https://github.com/ExplorViz/deployment.git
cd deployment/docker/
```

2\. Use `docker compose` to start ExplorViz' software environment and its services. The frontend is served via nginx and by default runs on port `8080`. You can change ports and hostnames in the (hidden) `.env` file.

```sh
docker compose up --pull=always -d
```

3\. Open [http://localhost:8080](http://localhost:8080) in your web browser, e.g. Mozilla Firefox.

4\. You will see a [Software Landscape](/3-architecture) called "Default Landscape" in a table. Click on the :octicons-info-24: icon to see the [Landscape Token](/3-architecture)'s (normally auto-generated) `value` and `secret`. This pair of data is used in the upcoming instrumentation configuration. With that, every incoming data record can be mapped to a user and the software landscape which is identified by the landscape token.

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

1\. Open [http://localhost:18080](http://localhost:18080) in your web browser and generate some load by clicking around.

2\. Open [http://localhost:8080](http://localhost:8080) in your web browser and click on "Default Landscape" to open the visualization of the Spring PetClinic's runtime behavior.

3\. The visualization is updated every tenth second and shows the aggregated runtime behavior of the Spring PetClinic.

4\. (Optional) Right click the white background to access the context menu.

5\. (Optional) On the top right corner you can find a button to open a sidebar. There you will find visualization settings and the collaboration tab that enables you to join or host a collaborative session.
