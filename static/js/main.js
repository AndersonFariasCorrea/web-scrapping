$(document).ready(function() {
    $("#searchButton").click(function() {
        var selectedSites = [];

        if ($("#kabumCheckbox").is(":checked")) {
            selectedSites.push("Kabum");
        }
        if ($("#OficinaDosBitsCheckbox").is(":checked")) {
            selectedSites.push("OficinaDosBits");
        }

        // if (selectedSites.length === 0) {
        //     alert("Por favor, selecione um hardware e marque pelo menos um site.");
        //     return;
        // }

        var pesquisa = $("#modelSearch").val()

        $.getJSON("/api", {"busca":pesquisa}, function(data) {
            $("#hardwareInfoBody").empty();

            if (data.status && data.status > 200) {
                alert(data.msg);
                return;
            }

            if(data[0]){
                sites = data.map(el => Object.keys(el)[0]);
            }

            sites.forEach(function(site) {
                if (data.filter(el => el[site])[0][site]) {
                    data.filter(el => el[site])[0][site].items.forEach(function(item) {
                        $("#hardwareInfoBody").append(
                            "<tr>" +
                            "<td>" + item.nome_item + "</td>" +
                            "<td>" + site + "</td>" +
                            "<td>" + item.valor_item + "</td>" +
                            "<td>" + item.valor_c_desconto + "</td>" +
                            "<td><a href='" + item.link + "' target='_blank'>Ver produto</a></td>" +
                            "</tr>"
                        );
                    });
                } else {
                    alert("Erro ao buscar dados do site " + site);
                }
            });
        }).fail(function(jqXHR, textStatus, errorThrown) {
            alert("Erro: " + textStatus + " - " + errorThrown);
        });
    });

    $("#sortByPriceButton").click(function() {
        var tbody = $("#hardwareInfoBody");
        var rows = tbody.find("tr").get();

        rows.sort(function(rowA, rowB) {
            var priceA = parseFloat($(rowA).find("td:eq(2)").text());
            var priceB = parseFloat($(rowB).find("td:eq(2)").text());
            return priceA - priceB;
        });

        $.each(rows, function(index, row) {
            tbody.append(row);
        });
    });
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