'use strict';

// Change these credentials to login:
let user = 'httpwatch';
let password = 'secret';

chrome.webRequest.onBeforeSendHeaders.addListener(function(details) {
	details.requestHeaders.push({name: "Authorization", value: "Basic " + btoa(unescape(encodeURIComponent(user + ':' + password)))});
	return { requestHeaders: details.requestHeaders };
	},
    {urls: ["<all_urls>"]},
	["blocking", "requestHeaders"]);
