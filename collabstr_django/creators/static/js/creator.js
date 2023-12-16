const platformFilterMap = {
    Instagram: 'IG',
    TikTok: 'TT',
    "User Generated Content": 'UGC'
}
const platformNameMap = {
    IG: 'Instagram',
    TT: 'TikTok',
    UGC: 'User Generated Content'
}

function generateCreatorCardHtml(creator) {
    var contentUrl = creator.contents.length > 0 ? creator.contents[0].url : '';
    var isVideo = contentUrl.endsWith('.mov') || contentUrl.endsWith('.mp4');
    var mediaHtml = isVideo ?
        `<video class="profile-listing-media" src="${contentUrl}" alt="content by ${creator.name}"></video><div class="video-tooltip">Video</div>` :
        `<img loading="lazy" class="profile-listing-img" src="${contentUrl}" alt="content by ${creator.name}">`;

    var creatorCardHtml = `
        <div class="influencer-card">
            <div class="profile-listing-img-holder">
                <div class="save-btn" data-profile-id="${creator.id}">
                    <svg xmlns="http://www.w3.org/2000/svg" height="30" width="30" viewBox="0 0 512 512">
                    <!-- !Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2023 Fonticons, Inc. -->
                    <path fill="white" d="M288 32c0-17.7-14.3-32-32-32s-32 14.3-32 32V274.7l-73.4-73.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l128 128c12.5 12.5 32.8 12.5 45.3 0l128-128c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L288 274.7V32zM64 352c-35.3 0-64 28.7-64 64v32c0 35.3 28.7 64 64 64H448c35.3 0 64-28.7 64-64V416c0-35.3-28.7-64-64-64H346.5l-45.3 45.3c-25 25-65.5 25-90.5 0L165.5 352H64zm368 56a24 24 0 1 1 0 48 24 24 0 1 1 0-48z" />
                    </svg>
                </div>
                ${mediaHtml}
                <div class="profile-listing-owner-holder">
                    <div class="profile-listing-owner-info-holder">
                        <div class="profile-listing-owner-name">${creator.name}</div>
                        <div class="profile-listing-owner-username">@${creator.username}</div>
                    </div>
                </div>
            </div>

            <div class="profile-listing-info-row">
                <div class="profile-listing-platform">${platformNameMap[creator.platform]}</div>
                <div class="profile-listing-rating">
                    <!-- SVG for rating here -->
                    <span>${creator.rating}</span>
                </div>
            </div>
        </div>
    `;

    return creatorCardHtml;
}

function loadCreators(page, platform) {
    var apiUrl = "/api/creator/";
    var query = {};
    if (platform) {
        query.platform = platformFilterMap[platform];
    }

    $.ajax({
        url: apiUrl,
        type: "GET",
        data: query,
        success: function (response) {
            $("#influencer-results").empty();
            response.results.forEach(function (creator) {
                if (!creator.first_content_url) {
                    creator.first_content_url = creator.contents.length > 0 ? creator.contents[0].url : '';
                }
                var creatorCardHtml = generateCreatorCardHtml(creator);
                $("#influencer-results").append(creatorCardHtml);
            });
        },
        error: function (error) {
            console.error("Error fetching creators:", error);
        }
    });
}
