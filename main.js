window.stop();

var script = document.createElement('script');
script.src = "https://challenges.cloudflare.com/turnstile/v0/api.js?onload=onloadTurnstileCallback";
document.head.appendChild(script);

// Create three div elements with unique IDs
for (var i = 1; i <= 3; i++) {
    var divId = 'new_captcha' + i;
    document.querySelector("body").innerHTML += "<div id='" + divId + "'></div>";

    (function (divId) {
        var intervalId;
        var isRendering = false;

        intervalId = setInterval(function () {
            if (isRendering) return;

            isRendering = true;
            var lk = false;

            turnstile.render('#' + divId, {
                sitekey: '0x4AAAAAAA28MYj-gETgmH3L', // site key بتاع الموقع بتاعهم
                tabindex: 0,
                callback: function (token) {
                    
                    const apiUrl = `http://127.0.0.1:2000/send_vote?captcha=${token}`;
                    fetch(apiUrl)
                        .then(response => {
                            if (response.ok) {
                                console.log("RESP IS",response.text)
                                console.log('GET request successful');
                                
                            } else {
                                console.error('GET request failed');
                            }
                        })
                        .catch(error => {
                            console.error('Error making the GET request:', error);
                        });
                    isRendering = false;
                    lk = true;
                },

            });

            setTimeout(function () {
                if (!lk) isRendering = false;
            }, 10000);
        }, 7000);
    })(divId);
}
