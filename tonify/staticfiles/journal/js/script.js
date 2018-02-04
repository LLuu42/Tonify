$(document).ready(function() {

    $("#form-submit").on("submit", function(e) {
        e.preventDefault();

        url = location.protocol + "//" + location.host + "/journal/returnPlaylist"

        var textarea = $('textarea#taskInput');
        var text = textarea.val();
        console.log(text);
        $.ajax({
            type: "POST",
            url: url,
            data: {
                "input": text,
            },
            beforeSend: function(xhr) {
                textarea.val('');
                $("#returned").empty();
                $("<p>loading...</p>").appendTo("#returned");
                console.log(text);
            }

        }).done(function(data) {
            console.log(JSON.stringify(data));
            $("#returned").empty();
            //$("<p>" + data["queryResult"]["fulfillmentText"] + "</p>").appendTo("#returned");
        });
    });
});
