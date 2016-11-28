'use strict';

describe('Ranker tests', function () {
    var $scope, controller;

    beforeEach(function () {
        module('RankingApp');

        inject(function ($controller, $rootScope) {
            $scope = $rootScope.$new();

            controller = $controller('RankingController', {
                $scope: $scope,
            });
        });
    });

    it('Test items is empty by default', function () {
        expect($scope.items).toEqual([]);
    });
});