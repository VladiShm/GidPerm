document.addEventListener("DOMContentLoaded", () => {
  const searchForm = document.getElementById("search-form");
  const searchInput = document.getElementById("search-input");
  const productCards = document.querySelectorAll(".product-card");

  searchForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const searchTerm = searchInput.value.toLowerCase();
    filterProducts(searchTerm);
  });

  function filterProducts(term) {
    productCards.forEach((card) => {
      const title = card.querySelector("h2").textContent.toLowerCase();
      const description = card.querySelector("p").textContent.toLowerCase();
      if (title.includes(term) || description.includes(term)) {
        card.style.display = "block";
      } else {
        card.style.display = "none";
      }
    });
  }
});
