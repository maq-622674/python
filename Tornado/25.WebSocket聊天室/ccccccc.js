var isLoaded = false;
function reqs(opts) {
    $.ajax({
        type: 'get',
        url: 'demo.php',
        dataType: 'json',
        beforeSend: function() {
            if(opts.init === 1) {
                $('.zh-loading').show();
            }
            isLoaded = false;
        },
        success: function(res) {
            console.log(res);
        },
        complete: function() {
            if(opts.init === 1) {
                $('.zh-loading').hide();
            }
            isLoaded = true;
        },
        error: function() {
            console.log('请求失败~');
        }
    });
}
reqs({"init": 1});
setInterval(function() {
    isLoaded && req({"init": 0});
}, 3000);