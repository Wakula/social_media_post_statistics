### Coding assignment
Implement an API to manage social media posts statistics (e.g Facebook).
The API is being used by a separate application that scans posts of a Facebook user and saves posts statistics (in our case just the number of likes for each post).

A post has the following properties: user id, post id, likes count.

The API needs to provide the following functionality for the application that scans Facebook:
Save statistics (the application will provide user id, post id and likes count).
Get latest statistics for a specific post id (respond with user id, post id, likes count).
Get latest statistics for all posts of a specific user id.

Time spent on test assignment - 2 hours:

### Short API description

POST api/post_statistics/

    Request Body:
    {
        "user_id": 1,
        "post_id": 2,
        "likes_count": 3
    }

GET api/post_statistics/retrieve_latest_by_post/?post_id=<post_id>

    Response Body:
    {
        "user_id": 12,
        "post_id": <post_id>,
        "likes_count": 4
    }

GET api/post_statistics/list_latest_by_user/?user_id=<user_id>

    Response Body:
    [
        {
            "user_id": <user_id>,
            "post_id": 1,
            "likes_count": 18
        },
        ...
    ]
