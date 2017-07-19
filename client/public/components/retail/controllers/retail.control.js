retail
    .controller('RetailController', function ($scope, Chain, Store, Employee, Login) {
        Chain.query().$promise.then(function (data) {
            $scope.chains = data;
        });
        Store.query().$promise.then(function (data) {
            $scope.stores = data;
        });
        Employee.query().$promise.then(function (data) {
            $scope.employees = data;
        });

        var data = {
            username: 'john',
            password: 'password'
        };
        Login.save({}, data,
            function (responsedata) {
                // possibly do stuff with result
                $scope.login = responsedata;
            },
            function (reply) {
                // Comments on best way to access $scope here are welcome.
                //  This feels a bit weird to me.
                $scope.info.errorMessage = reply.statusText;
            }
        );

        // $scope.login = $resource('http://localhost:8000/login/').post('http://localhost:8000/login/',data);
        // Login.query().$promise.then(function (data) {
        //     $scope.login = data;
        //     // var loginService = Login.save({}, data,
        //     //     function (responsedata) {
        //     //         // possibly do stuff with result
        //     //         $scope.login = responsedata;
        //     //     },
        //     //     function (reply) {
        //     //         // Comments on best way to access $scope here are welcome.
        //     //         //  This feels a bit weird to me.
        //     //         $scope.info.errorMessage = reply.statusText;
        //     //     }
        //     // );
        // });
    });

