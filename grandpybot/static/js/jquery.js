function initMap(latitude, longitude, is_call = false) {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: {
            lat: 48.8534,
            lng: 2.3488
        }
    });
    if (is_call == true) {
        var zoom = 18;
        var position = {
            lat: parseFloat(latitude),
            lng: parseFloat(longitude)
        };
        var center = position
        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: zoom,
            center: position
        });
        map.setMapTypeId('hybrid');
        var marker = new google.maps.Marker({
            position: position,
            map: map
        });
    }
}

function display_error(type_error) {
    $('#tchat').append($('#alert').css("display", "block"));
    if (type_error == "description") {
        $('#text_error').text("Je ne connais pas d'histoire sur ce que tu me demande jeune ami ");
    } else if (type_error == "place") {
        $('#text_error').text("Hum cette carte est introuvable... Je dois me faire vieux! ");
    } else {
        $('#text_error').text("Je ne connais ni l'histoire ni l'adresse de ce que tu me demandes jeune ami");
    }
}


$(function() {

    $('#boutenvoyer').click(function() {
        $('#alert').css("display", "none");
        var msg = '<br>' + '<msg>' + "&nbsp;Vous → " + $('#msg_id').val() + '</msg>' + '<br>';
        var request = $('input');
        if ($('#input_form').val() != '') {
            $('#tchat').append(msg);
            $('#contain_loader').css("display", "block");
            $.ajax({
                url: '/get_user_request',
                data: $(request).serialize(),
                type: 'GET',
                success: function(response) {
                    $('#contain_loader').css("display", "none");
                    var response_json = JSON.parse(response);
                    if (response_json['type_search'] == 'place') {
                        adresse = response_json['emplacement']['adresse'];
                        $('#tchat').append('<br>' + '<reponse>' + ("&nbsp;Grandpy → " + response_json['sentance_place']) +
                            '<hr>' + adresse + '<br><hr>');
                        latitude = response_json['emplacement']['latitude']
                        longitude = response_json['emplacement']['longitude']
                        initMap(latitude, longitude, true)
                        $('#tchat').append(display_error("description"));
                    } else if (response_json['type_search'] == 'description') {
                        $('#tchat').append('<br>' + '<reponse>' + ("&nbsp;Grandpy → " + response_json['sentance_description'] + response_json['description']) + ' ... ' +
                            '<br>' + "Plus de détails sur wikipedia → " + '<a href="' + (response_json['wiki_url']) + '">' + (response_json['wiki_url']));
                        $('#tchat').append(display_error("place"))
                    } else if (response_json['type_search'] == 'place description') {
                        adresse = response_json['emplacement']['adresse'];
                        $('#tchat').append('<br>' + '<reponse>' + ("&nbsp;Grandpy → " + response_json['sentance_place']) +
                            '<hr>' + adresse + '<br><hr>' + (response_json['sentance_description'] + response_json['description']) + ' ... ' +
                            '<br>' + "Plus de détails sur wikipedia → " + '<a href="' + (response_json['wiki_url']) + '">' + (response_json['wiki_url']) + '</a>');
                        latitude = response_json['emplacement']['latitude']
                        longitude = response_json['emplacement']['longitude']
                        initMap(latitude, longitude, true)
                    } else {
                        $('#tchat').append(display_error());
                    }
                },
                error: function(error) {
                    display_error();
                }
            });
        }
    });
    $('#msg_id').keypress(function(e) {
        var key = e.which;
        if (key == 13) // the enter key code
        {
            $('#boutenvoyer').click();
            return false;
        }
    });
});