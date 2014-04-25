


/*
$(document).ready(function() {
        alert("wuha");
        var myDataRef = new Firebase('https://dazzling-fire-9098.firebaseio.com/');
        var auth = new FirebaseSimpleLogin(myDataRef, function(error, user) {
            if (!error) {
            // Success!
            }
            else{
                console.log("FIREBASE ERROR: " + error + " " + user);
            }
        });

        auth.login('password', {
          email: 'guangzhegao@gmail.com',
          password: 'root'
        });


        // listen other user sends
        myDataRef.child( {{ user.id }} + "/msg_recv").on("child_added",
        function(newMessageSnapshot) {
            //renderNotification(newMessageSnapshot.val());
            //newMessageSnapshot.ref().remove();
            incomeMSG = newMessageSnapshot.val()
            $("ul.notification-list").append('<a class="list-group-item head-dropdown-menu-heading notification-item" href="#" id="'+ incomeMSG.id_sender +'">'+
                {{user.get(incomeMSG.id_sender)}}+ ": " + incomeMSG.info_sender + '</a>');
        });


        //Send a message to another user, should be be called by places necessary(new stuff is done)
var notify_users = function (initiator, users_affected, information){
    affected_len = users_affected.length
    for(i=0; i<affected_len; ++i){
        myDataRef.child(users_affected[i]).child("msg_recv").push({id_sender: initiator, info_sender: information });
    }
}

        //remove the notification when be read
        $("a.notification-item")
        $(document.body).on("click", "a.notification-ack", function(e){
            e.preventDefault();
            myDataRef.child( {{ user.id }} + "/msg_recv").remove(); //remove all aknowledgements in db

            $("ul.notification-lsit").html('<a class="list-group-item head-dropdown-menu-heading notification-item" href="#">Acknowledge</a>'); //remove all aknowledgements in html
        });


        function renderNotification(incomeMSG){
            id_sender = incomeMSG.id_sender;
            info_sender = incomeMSG.info_sender;
        }

});
*/