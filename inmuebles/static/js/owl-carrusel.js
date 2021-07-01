$(".owl-carousel").owlCarousel({
    autoplay: false,
    autoplayhoverpause: false,
    responsive: {
        0: {
            items: 1,
            dots: false
        },
        485: {
            items: 2,
            dots: false
        },
        720: {
            items: 3,
            dots: true
        },
        1100: {
            items: 4,
            dots: true
        },
        1500: {
            items: 5,
            dots: true
        },
    }
});