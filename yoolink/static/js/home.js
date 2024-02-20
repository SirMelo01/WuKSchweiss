const realmap = document.querySelector("#map");
const covermap = document.querySelector("#covermap");

var map;



//Map

function mapLoad() {
  console.log("ARSCH");
  if (cookiemapselect === null || cookiemapselect === "false") {
    covermap.classList.remove("hidden");
    realmap.classList.add("hidden");
  } else {
    covermap.classList.add("hidden");
    realmap.classList.remove("hidden");

    // Karte wird geladen
    map.setView([48.6987771, 13.1176147], 13);
    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 19,
      attribution:
        '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    }).addTo(map);
    var marker = L.marker([48.698771, 13.1176147]).addTo(map);
    map.scrollWheelZoom.disable();
  }
}



//FQA
$(document).ready(function() {
  $(".faq-toggle").click(function() {
    var content = $(this).siblings(".faq-content");
    var arrow = $(this).find(".faq-arrow");
    
    if (content.hasClass("hidden")) {
      content.removeClass("hidden");
      arrow.addClass("rotate-180");
    } else {
      content.addClass("hidden");
      arrow.removeClass("rotate-180");
    }
  });
});

setTimeout(() => {
  if (cookiemapselect !== null && cookiemapselect !== "false") {
    map = L.map("map");
    map.on("focus", function () {
      map.scrollWheelZoom.enable();
    });
    map.on("blur", function () {
      map.scrollWheelZoom.disable();
    });
  }
  mapLoad();
}, 500);
