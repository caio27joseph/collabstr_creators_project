var apiUrl = "http://127.0.0.1:8000";

export function loadCreators(page = 1, platform = "") {
    return $.ajax({
        url: apiUrl + "/api/creator/",
        type: "GET",
        data: {
            page: page,
            platform: platform,
        },
        dataType: "json",
    });
}
