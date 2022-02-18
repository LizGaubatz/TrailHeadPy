function editButton(formId) {
    
    var x = document.getElementById(formId);
    console.log(x)
    x.classList.toggle('edit-form')
}

// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
let map;
let service;
let infowindow;

function initMap() {
    const thc = new google.maps.LatLng(39.06511, -108.585886);

    infowindow = new google.maps.InfoWindow();
    map = new google.maps.Map(document.getElementById("map"), {
        center: thc,
        zoom: 15,
    });

    const request = {
        query: "trailhead coffee bar and cafe",
        fields: ["name", "rating", "user_ratings_total", "geometry", "formatted_address"],
    };

    service = new google.maps.places.PlacesService(map);
    service.findPlaceFromQuery(request, (results, status) => {
        if (status === google.maps.places.PlacesServiceStatus.OK && results) {
            console.log('hi')
            for (let i = 0; i < results.length; i++) {
                createMarker(results[i]);
            }
            console.log(results[0])
            map.setCenter(results[0].geometry.location);
        }
    });
}

function createMarker(place) {
    if (!place.geometry || !place.geometry.location) return;

    const marker = new google.maps.Marker({
        map,
        position: place.geometry.location,
    });

    const infowindow = new google.maps.InfoWindow();

    console.log(place)

    google.maps.event.addListener(marker, "click", () => {
        const content = document.createElement("div");
        const nameElement = document.createElement("h2");

        nameElement.textContent = place.name;
        content.appendChild(nameElement);

        const ratingElement = document.createElement("h1")

        ratingElement.textContent = place.rating;
        content.appendChild(ratingElement)

        const userRatingElement = document.createElement("p");

        userRatingElement.textContent = place.user_ratings_total;
        content.appendChild(userRatingElement)

        const placeAddressElement = document.createElement("p");

        placeAddressElement.textContent = place.formatted_address;
        content.appendChild(placeAddressElement);
        infowindow.setContent(content);
        infowindow.open(map, marker);
    })
}







// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
// function initMap() {
//     const map = new google.maps.Map(document.getElementById("map"), {
//         center: { lat: 39.06511, lng:  -108.585886 },
//         zoom: 15,
//     });
//     const request = {
//         placeId: "ChIJvVrDz-wcR4cROIqZGhL07fU",
//         fields: ["name", "formatted_address", "geometry", "rating"],
//     };
//     //     const request = {
//     //     placeId: "ChIJvVrDz-wcR4cROIqZGhL07fU",
//     //     fields: ["name", "rating", "user_ratings_total", "geometry", "price_level", "place_id", "formatted_address"],
//     // };
//     const infowindow = new google.maps.InfoWindow();
//     const service = new google.maps.places.PlacesService(map);

//     service.getDetails(request, (place, status) => {
//         console.log(place)
//         if (
//             status === google.maps.places.PlacesServiceStatus.OK &&
//             place &&
//             place.geometry &&
//             place.geometry.location
//         ) {
//             const marker = new google.maps.Marker({
//                 map,
//                 position: place.geometry.location,
//             });

//             google.maps.event.addListener(marker, "click", () => {
//                 const content = document.createElement("div");
//                 const nameElement = document.createElement("h2");

//                 nameElement.textContent = place.name;
//                 content.appendChild(nameElement);

//                 const ratingElement = document.createElement("h1")

//                 ratingElement.textContent = place.rating;
//                 content.appendChild(ratingElement)

//                 const placeAddressElement = document.createElement("p");

//                 placeAddressElement.textContent = place.formatted_address;
//                 content.appendChild(placeAddressElement);
//                 infowindow.setContent(content);
//                 infowindow.open(map, marker);
//             });
//         }
//     });
// }