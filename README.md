# Getting Started
  This document explains how to successfully call the Category-Product API with your web browser and get data of Product and Category objects. It assumes you know how to perform REST API calls.

 **Before You Start**
----
  You will need to complete the following steps.

   * Download this github-repository.
   * Install the dependancies.
   * Run the Django-server.
   
   ### 1. Download this github-repository.

   ```bash
   $ git clone https://github.com/HMHarris-git/Assignment.git
   ```

   ### 2. Installing the dependancies.

   * Enter the directory with ` requiements.txt` file.

   ```bash
   $ cd Assignment
   ```
   * Installing the  dependancies.

   ```bash
    $ pip install -r requirements.txt
   ```

  ### 3. Run the Django-Server. 
   * Change directory to one with `manage.py` file.

   ```bash
   $ cd assignment_site
   ```
   * Run the server using following command.

   ```bash
   $ python manage.py runserver
   ```


# Category-Product API

  This API return a json data with category and product details. It can also be used for performing CRUD operations on data.

**Show All Categories**
----
  Returns json about all categories. As well as provides option to create a new category object.

* **URL**

  `api/categories/`

* **Method:**
  

  `GET` | `POST`
  
*  **URL Params**

   **Required:**
 
   None

* **Data Params**

  Body Payload for `POST` request.
  ```json
  {
        "name": "Data"
  } 
  ```

* **Success Response:**
  

  * **Code:** 200 <br />
    **Content:** 
    ```json
    [
    {
        "id": 1,
        "name": "shoes"
    },
    {
        "id": 2,
        "name": "data"
    }
]
    ```

* **Sample Call: (Using Postman)**
  
  * GET request

  <img src="postman_testing_images\Get_request_to_api-categories.png">

  * POST request
  
  <img src="postman_testing_images\Post_request_to_api-categories.png">

**Show Category**
----
  Returns json data regarding single category based on category ID. As well as provides option to perform RUD (Retrieve, Update, Delete) operations on selected category object.

* **URL**

  `api/categories/:id`

* **Method:**

  `GET` | `DELETE` | `PUT`
  
*  **URL Params**

   **Required:**
 
   `id=[integer]`

* **Data Params**

  Body Parameters for `PUT` request (Parameters can be referred in images provided).
  ```json
  {
        "name": "Movies"
  } 
  ```

* **Success Response:**
  

  * **Code:** 200 <br />
    **Content:** 
    ```json
    {
       "id": 2,
       "name": "data"
    }
    ```

* **Sample Call: (Using Postman)**
  
  * GET request to `api/categories/1`

  <img src="postman_testing_images\Get_request_to_api-categories-1.png">

  * PUT request to `api/categories/1`
  
  <img src="postman_testing_images\PUT_request_to_api-categories-1.png">

  * DELETE request to `api/categories/1`
  
  <img src="postman_testing_images\DELETE_request_to_api-categories-1.png">

---
**Show All Products**
----
  Returns json data about all Products. As well as provides option to create a new Product object.

* **URL**

  `api/products/`

* **Method:**
  

  `GET` | `POST`
  
*  **URL Params**

   **Required:**
 
   None

* **Data Params**

  Body Payload for `POST` request (Parameters can be refered in images). 
  ```json
  {
        "name": "Morbius",
        "category": [4,7],
        "price": 20,
        "stock": 1
    }
  ```

* **Success Response:**
  

  * **Code:** 200 <br />
    **Content:** 
    ```json
    [
    {
        "id": 1,
        "name": "pole",
        "category": [],
        "price": 0.0,
        "stock": 0
    },
    {
        "id": 2,
        "name": "Morbius",
        "category": [
            4,
            7
        ],
        "price": 20.0,
        "stock": 1
    }
]
    ```

* **Sample Call: (Using Postman)**
  
  * GET request

  <img src="postman_testing_images\GET_request_to_api-products.png">

  * POST request
  
  <img src="postman_testing_images\POST_request_to_api-products.png">

**Show Product**
----
  Returns json data regarding single product based on category ID. As well as provides option to perform RUD (Retrieve, Update, Delete) operations on selected product object.

* **URL**

  `api/products/:id`

* **Method:**

  `GET` | `DELETE` | `PUT`
  
*  **URL Params**

   **Required:**
 
   `id=[integer]`

* **Data Params**

 Body Parameters for `PUT` request (Parameters can be referred in images).
  ```json
  {
    "name": "pole",
    "category": [6,7],
    "price": 24.0,
    "stock": 88
}
  ```

  

* **Success Response:**
  

  * **Code:** 200 <br />
    **Content:** 
    ```json
    {
        "id": 1,
        "name": "pole",
        "category": [],
        "price": 0.0,
        "stock": 0
        }
    ```

* **Sample Call: (Using Postman)**
  
  * GET request to `api/products/1`

  <img src="postman_testing_images\GET_request_to_api-products-1.png">

  * PUT request to `api/products/1`
  
  <img src="postman_testing_images\PUT_request_to_api-products-1.png">

  * DELETE request to `api/products/1`
  
  <img src="postman_testing_images\DELETE_request_to_api-products-1.png">

  * After Deleting the objects GET request to `api/products/`

  <img src="postman_testing_images\after_Delete_GET_request_to_api-products.png">


* **Tasks accomplished in API:**
  
  * Add a category
  * Add Product mapped to a category or categories.
  * Get all categories.
  * Get all products with list of categories mapped to it.
  * Update product details (name, price etc.)

----  
