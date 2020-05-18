var session = null;

document.addEventListener("DOMContentLoaded", function(event) {

    QiSession(function (s) {
        console.log("connected!");
        session = s;

        // Subscribe to the MenuChosen event and then show the menu on the screen
        session.service("ALMemory").then(function(mem) {
            // mem.subscriber("ColorsDemo/ColorChosen").then( function (sub) {
            //     sub.signal.connect(colorCallback);
            // });
            mem.subscriber("TabChosen/Name").then( function (tts) {
                sub.signal.connect(tabCallback);
            });

        });


    }, function () {
        console.log("disconnected");
    })
});

function raiseEvent(value) {
    console.log("Choosing tab: ", value);
    session.service("ALMemory").then(function (mem) {
        mem.raiseEvent("TabChosen/Name", value);
        //mem.raiseEvent("ButtonChosen/Name", value);
    });
}


function tabCallback(tab) {
    console.log("a new tab has been selected:", tab);
    if (tab === 'drinks') {
        document.getElementById("tab").src="imgs/drinks.jpg";
        document.getElementById("orderForm").style.width = "0%";
        // session.service("ALTextToSpeech").then(function (tts) {
        //         tts.say("Yes, lets start off with a drink for you. We have a range of alcoholic and Non alcoholic drinks");
        // });
        session.service("ALDialog").then(function (dlg) {
                dlg.forceInput("show me drinks");
        });
    }
    if (tab === 'menu') {
        document.getElementById("tab").src="imgs/starter_main.jpg";
        document.getElementById("orderForm").style.width = "0%";
        session.service("ALDialog").then(function (dlg) {
                dlg.forceInput("Show me Menu");
        })
    }

    if (tab === 'deserts') {
        document.getElementById("tab").src="imgs/deserts.jpg";
        document.getElementById("orderForm").style.width = "0%";
        session.service("ALDialog").then(function (dlg) {
                dlg.forceInput("show me desserts");
        })
    }

    if (tab === 'home') {
        document.getElementById("tab").src="imgs/lakeside_header.jpg";
        document.getElementById("orderForm").style.width = "0%";
    }

    if (tab === 'orderHere')
        document.getElementById("orderForm").style.width = "100%";

    }

function openNav() {
  document.getElementById("orderForm").style.width = "100%";
}

function closeNav() {
  document.getElementById("orderForm").style.width = "0%";
}

function openOrderForm(evt, menuName) {
  var i, order_selection_tab, order_links;
  order_selection_tab = document.getElementsByClassName("order_selection_tab");
  for (i = 0; i < order_selection_tab.length; i++) {
    order_selection_tab[i].style.display = "none";
  }
  order_links = document.getElementsByClassName("order_links");
  for (i = 0; i < order_links.length; i++) {
    order_links[i].className = order_links[i].className.replace(" active", "");
  }
  document.getElementById(menuName).style.display = "block";
  evt.currentTarget.className += " active";
}

function drinkTab(evt, drinkType) {
  var i, drinkTab, drink_links;
  drinkTab = document.getElementsByClassName("drinkTab");
  for (i = 0; i < drinkTab.length; i++) {
    drinkTab[i].style.display = "none";
  }
  drink_links = document.getElementsByClassName("drink_links");
  for (i = 0; i < drink_links.length; i++) {
    drink_links[i].className = drink_links[i].className.replace(" active", "");
  }
  document.getElementById(drinkType).style.display = "block";
  evt.currentTarget.className += " active";
}

// function raiseEvent(value) {
//     console.log("Choosing color: ", value);
//     session.service("ALMemory").then(function (mem) {
//         mem.raiseEvent("ColorsDemo/ColorChosen", value);
//     });
// }

function addItem(name) {
    var newElement = document.createElement('LI');
    var list = document.getElementById("the_order");
    list.appendChild(newElement);
    newElement.innerHTML = name + "<button class='btn'>&times;</button>";
    newElement.addEventListener('click', function () {
        this.parentNode.removeChild(this);
    });
}


function removeAllOptions(){
    var ul = document.getElementById("the_order");
    ul.innerHTML = '';
}


function sendOrder(){
    // TODO: send to a server and show a confirmation of sent.
    var ul = document.getElementById("the_order");
    ul.innerHTML = "<br><h2>Thanks!</h2><h2>Your order has been sent!</h2><br><button class=ordering_buttons1 onclick='removeAllOptions()'>Click here to add to your order</button><br>";
}

function dropDown(element) {
  var dropdowns = document.getElementsByClassName("dropdown-content");
  var i;
  for (i = 0; i < dropdowns.length; i++) {
    dropdowns[i].classList.remove('show');
  }
  // element.nextSibling is the carriage return… need to go to the next next to point on the dropdown menu
  element.nextSibling.nextSibling.classList.toggle("show");
  //


}

function speech(text) {
   session.service("ALDialog").then(function (dlg) {
       dlg.forceInput(text);
   })
}