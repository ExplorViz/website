(function () {
  var STORAGE_KEY = "explorviz-external-content";

  function hasConsent() {
    try {
      return localStorage.getItem(STORAGE_KEY) === "accepted";
    } catch (error) {
      return false;
    }
  }

  function saveConsent() {
    try {
      localStorage.setItem(STORAGE_KEY, "accepted");
    } catch (error) {
      /* ignore storage failures */
    }
  }

  function clearConsent() {
    try {
      localStorage.removeItem(STORAGE_KEY);
    } catch (error) {
      /* ignore storage failures */
    }
  }

  function loadBlock(block) {
    block.querySelectorAll("iframe[data-src]").forEach(function (iframe) {
      iframe.src = iframe.getAttribute("data-src");
    });

    block.classList.add("external-content-block--loaded");
  }

  function unloadBlock(block) {
    block.querySelectorAll("iframe[src]").forEach(function (iframe) {
      iframe.setAttribute("data-src", iframe.getAttribute("src"));
      iframe.removeAttribute("src");
    });

    block.classList.remove("external-content-block--loaded");
  }

  function initBlock(block) {
    var acceptButton = block.querySelector(".external-content-block__accept");
    var revokeButton = block.querySelector(".external-content-block__revoke");

    if (acceptButton) {
      acceptButton.addEventListener("click", function () {
        saveConsent();
        loadBlock(block);
      });
    }

    if (revokeButton) {
      revokeButton.addEventListener("click", function () {
        clearConsent();
        unloadBlock(block);
      });
    }

    if (hasConsent()) {
      loadBlock(block);
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".external-content-block").forEach(initBlock);
  });
})();
