# DevOps Assignment
Creating an application using DevOps style

Creating a simple web application using weatherapi.

**Automated building, testing, deployment to heroku is implemented**

1. The repository has been added with CI/CD pipeline (created **workflows** for push commit using **github actions** https://github.com/rbadrin/DevOps/actions/runs/1430694830/workflow).

    -> Unit testing was done using pytest   
        
        a) Simple assertion
        
        b) Assertion based on status code from api
  
2. Created an issue and closed it.

3. Deployed the application on heroku cloud platform ( https://ancient-bayou-70234.herokuapp.com/   
                                                       https://ancient-bayou-70234.herokuapp.com/getWeather).

   The automated deployment happens only on the main branch (https://github.com/rbadrin/DevOps/actions).

4. Created an **Docker Image** for the python app (https://hub.docker.com/repository/docker/badri311/pythonapp).

5. The working branch,api_call, mastercopy and mastercopyapi was created for testing and to create a pull request and merge it with the main branch.

6. Created Github Secrets for heroku api access. 








