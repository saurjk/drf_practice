retail
    .factory('Login', function ($resource) {
        return $resource(
            'http://localhost:8000/login/',
            {},
            {
                'query': {
                    method: 'POST',
                    isArray: true,
                    headers: {
                        'Content-Type': 'application/json'
                    }
                }
            },
            {
                stripTrailingSlashes: false
            }
        );
    });