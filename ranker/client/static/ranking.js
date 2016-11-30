var rankingApp = angular.module('RankingApp', []);

rankingApp.controller('RankingController', function ($scope, $http) {
    $scope.items = [];

    $http({
        method: 'GET',
        url: '/items/'
    }).then(success, error);

    function success(response) {
        console.log(response.data);
        $scope.items = response.data;
    }

    function error(response) {
        console.log('Error retrieving items.');
    }
});