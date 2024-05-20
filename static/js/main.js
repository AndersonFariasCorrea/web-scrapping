$(document).ready(function() {
    $("#searchButton").click(function() {
        var selectedHardware = $("#hardwareSelect").val();
        var selectedSites = [];

        if ($("#kabumCheckbox").is(":checked")) {
            selectedSites.push("Kabum");
        }
        if ($("#pichauCheckbox").is(":checked")) {
            selectedSites.push("Pichau");
        }

        if (selectedHardware === null || selectedSites.length === 0) {
            alert("Por favor, selecione um hardware e marque pelo menos um site.");
            return;
        }

        $.getJSON("busca.json", function(data) {
            $("#hardwareInfoBody").empty();

            selectedSites.forEach(function(site) {
                if (data[site] && data[site].itens) {
                    data[site].itens.forEach(function(item) {
                        $("#hardwareInfoBody").append(
                            "<tr>" +
                            "<td>" + item.nome_item + "</td>" +
                            "<td>" + site + "</td>" +
                            "<td>" + item.valor_item + "</td>" +
                            "<td>" + item.memoria_tamanho + "</td>" +
                            "<td>" + item.memoria_tipo + "</td>" +
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