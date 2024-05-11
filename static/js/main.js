$(document).ready(() => {
    console.log("Hello world!");
});


function get(fn, method, data) {
    return new Promise(function(resolve, reject) {
        data = data ?? '';
        $.ajax({
            url: `${fn}`,
            method: method,
            data: data,
            dataType: 'json'
        }).done(function(result) {
            if (Object.keys(result).length > 0) {
                resolve(result);
            } else {
                resolve([]);
            }
        }).fail(function(jqXHR, textStatus, errorThrown) {
            console.error('An error occurred, status:', textStatus);
            console.error('An error occurred, jqXHR:', jqXHR);
            reject([]);
        });
    }).catch(function(error) {
        console.error('Error or empty result:', error);
        return [];
    });
}