/*  Theme 
 *  Javascript actions, methods, and functions
 *  @package 
 *  @version 1.0
 */
$(function() {
    "use strict";
    /**
     * [wowInit initialize WOW Js]
     */
    function wowInit() {
        new WOW().init();
    }
    /**
     * [tickerInit initialize ticker Js]
     */
    function tickerInit() {
        $('#js-news').ticker({
            speed: 0.10, // The speed of the reveal
            // ajaxFeed: false,       // Populate jQuery News Ticker via a feed
            // feedUrl: false,        // The URL of the feed
            // MUST BE ON THE SAME DOMAIN AS THE TICKER
            // feedType: 'xml',       // Currently only XML
            // htmlFeed: true,        // Populate jQuery News Ticker via HTML
            // debugMode: true,       // Show some helpful errors in the console or as alerts
            // SHOULD BE SET TO FALSE FOR PRODUCTION SITES!
            controls: true, // Whether or not to show the jQuery News Ticker controls
            titleText: 'EM DESTAQUE', // To remove the title set this to an empty String
            displayType: 'reveal', // Animation type - current options are 'reveal' or 'fade'
            direction: 'ltr', // Ticker direction - current options are 'ltr' or 'rtl'
            pauseOnItems: 2000, // The pause on a news item before being replaced
            // fadeInSpeed: 600,      // Speed of fade in animation
            // fadeOutSpeed: 300      // Speed of fade out animation}
        });
    }
    /**
     * [mixItUpInit initialize mixItUp Js]
     */
    function mixItUpInit() {
        $('.filter-container').mixItUp({
            animation: {
                enable: true
            },
            load: {
                filter: '.category-1'
            }
        });

    }
    /**
     * [ripplIenit initialize rippl Js]
     */
    function ripplIenit() {
        $('*[data-color]').ripple({
            'v_duration': 1000,
            'h_duration': 1000
        });
    }

    /**
     * [scrollTop scroll to top page]
     */
    function scrollTop() {
        ('body').on('click', '#scroll-top', function() {
            $("html, body").animate({
                scrollTop: 0
            }, '1000');
        });
    }
    /**
     * [searchNavbar open and close search in the navbar ]
     */
    function searchNavbar() {
        $('body').on('click', '.search-link', function(event) {
            $('.search-screen').fadeIn(500);
            $('.page').addClass('blur');
            $('body').addClass('overflow-hidden');
        });

        $('body').on('click', '.search-close', function(event) {
            $('.search-screen').fadeOut(500, function() {
                $('body').removeClass('overflow-hidden');
            });
            $('.page').removeClass('blur');
        });
        $('body').on('click', '.open-search', function(event) {
            $('.main-search').toggle(100);
            $('.open-search').find('.fa-times').toggleClass('hide');
            $('.open-search').find('.fa-search').toggleClass('hide');
            return false;
        });
    }
    /**
     * light box options 
     */
    lightbox.option({
        'resizeDuration': 200,
        'wrapAround': true,
        'disableScrolling': true
    });


    /**
     * [arrInstagramFactory description]
     * @param  {[type]} json [description]
     * @return {[type]}      [description]
     */
    function arrInstagramFactory(json, numberOfimages) {
        var arrThumbnail = [];
        var arrHightResolution = [];
        // create array of thumbnil
        for (var i = 0; i < numberOfimages; i++) {
            arrThumbnail.push(json.items[i].images.thumbnail.url);
        }

        // create array of big images
        for (var x = 0; x < numberOfimages; x++) {
            arrHightResolution.push(json.items[x].images.standard_resolution.url);
        }
        return [arrThumbnail, arrHightResolution];
        // return json.items[0].images.low_resolution.url;
    }
    /**
     * [drawInstaImages draw Instagram Images inside sidebar]
     * @param  {[type]} arr [description]
     * @return {[type]}     [description]
     */
    function drawInstaImages(arr) {
        for (var i = 0; i < arr[0].length; i++) {
            console.log(arr[0][i]);
            var c = '<a class="gallery-small-image" href="' + arr[1][i] + '" data-lightbox="example-instagram10" data-title=""><img src="' + arr[0][i] + '" alt=""><i class="fa fa-search-plus "></i></a>';
            $(".gallery-block-small .images-container").prepend(c);
        }
    }

    function getImagesFromInstagram(userId, numerOfImages, accessToken) {

        $.ajax({
                // url: 'https://www.instagram.com/'+userId+'/media',
                url: 'https://api.instagram.com/v1/users/' + userId + '/media/recent/?access_token=' + accessToken,
                type: 'GET',
                dataType: 'json',
                // data: {param1: 'value1'},
            })
            .done(function(result) {
                console.log("success");
                drawInstaImages(
                    arrInstagramFactory(result, numerOfImages)
                );
                // console.log(arrInstagramFactory(result));
            });
        // .fail(function() {
        //     console.log("insta error");
        // })
        // .always(function() {
        //     console.log("insta complete");
        // });
    }

    // getImagesFromInstagram('khaledsamir1', 8,accessToken);
    // wowInit();
    tickerInit();
    mixItUpInit();
    ripplIenit();
    searchNavbar();

});
