# Foodtruckers API

REST API for the Foodtruckers App

# Endpoints

## Foodtrucks

### GET /api/v1/foodtrucks/

List all the foodtrucks registered.

#### Response sample:

HTTP Status Code: 200
```json
[
    {
        "id": 1,
        "facebook": "http://www.facebook.com/some_foodtruck",
        "food_type": "Tacos",
        "location": "19.432608,-99.133208",
        "name": "Happy Tacos",
        "photo": "http://localhost:8000/media/photo.jpg",
        "price": 80,
        "rating": 5,
        "twitter": "http://twitter.com/some_foodtruck",
        "location_object": {
            "lat": "19.432608",
            "long": "-99.133208"
        }
    },
    {
        "id": 2,
        "facebook": "http://facebook.com/other_foodtruck",
        "food_type": "Burgers",
        "location": "19.234521,-99.114567",
        "name": "Happy Burger",
        "photo": "http://localhost:8000/media/burgers.jpg",
        "price": 40,
        "rating": 4,
        "twitter": "http://twitter.com/other_foodtruck",
        "location_object": {
            "lat": "19.234521",
            "long": "-99.114567"
        }
    }
]
```

### GET /api/v1/foodtrucks/{pk}/

List an specific foodtruck based on its primary key.

#### Response sample.

HTTP Status Code: 200
```json
{
  "id": 1,
  "facebook": "http://www.facebook.com/some_foodtruck",
  "food_type": "Tacos",
  "location": "19.432608,-99.133208",
  "name": "Happy Tacos",
  "photo": "http://localhost:8000/media/photo.jpg",
  "price": 80,
  "rating": 5,
  "twitter": "http://twitter.com/some_foodtruck",
  "location_object": {
    "lat": "19.432608",
    "long": "-99.133208"
  }
}
```

### GET /api/v1/foodtrucks/{pk}/comments/

List the comments of a foodtruck.

#### Response sample.

HTTP Status Code: 200
```json
[
    {
        "id": 1,
        "user": "a username",
        "foodtruck": 1,
        "comment": "Me late esta foodtruck",
        "date_added": "2015-11-27",
        "likes": 0
    }
]
```

## Users

### GET /api/v1/users/

List all users regustered.

#### Response sample.

HTTP Status Code: 200
```json
[
    {
        "email": "oshardy3@gmail.com",
        "profile_picture": null
    }
]
```

### GET /api/v1/users/{pk}/

List the detail of a single user.

#### Response sample

HTTP Status Code: 200
```json
{
    "email": "oshardy3@gmail.com",
    "profile_picture": null
}
```
