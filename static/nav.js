document.addEventListener("DOMContentLoaded", () => {
  const nav = document.querySelector(".ev-nav");
  const navLinks = document.getElementById("navLinks");
  
  if (nav && navLinks) {
    // Create the hamburger menu toggle button
    const toggleBtn = document.createElement("button");
    toggleBtn.className = "ev-menu-toggle";
    toggleBtn.id = "menuToggle";
    toggleBtn.setAttribute("aria-label", "Toggle navigation");
    toggleBtn.innerHTML = '<i class="ti ti-menu"></i>';
    
    // Insert it right after the logo (before navLinks)
    const logo = nav.querySelector(".ev-logo");
    if (logo) {
      logo.after(toggleBtn);
    } else {
      nav.insertBefore(toggleBtn, navLinks);
    }
    
    // Handle toggle click
    toggleBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      const isExpanded = navLinks.classList.toggle("mobile-show");
      
      // Toggle the menu/close icon
      const icon = toggleBtn.querySelector("i");
      if (isExpanded) {
        icon.className = "ti ti-x";
      } else {
        icon.className = "ti ti-menu";
      }
    });
    
    // Close the navigation list if clicked outside
    document.addEventListener("click", (e) => {
      if (!nav.contains(e.target) && navLinks.classList.contains("mobile-show")) {
        navLinks.classList.remove("mobile-show");
        toggleBtn.querySelector("i").className = "ti ti-menu";
      }
    });

    // Handle mobile dropdown toggle on tap
    const dropdownBtn = nav.querySelector(".ev-dropdown-btn");
    const dropdownContent = nav.querySelector(".ev-dropdown-content");
    if (dropdownBtn && dropdownContent) {
      dropdownBtn.addEventListener("click", (e) => {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          e.stopPropagation();
          const isVisible = window.getComputedStyle(dropdownContent).display !== "none";
          dropdownContent.style.display = isVisible ? "none" : "block";
        }
      });
    }
  }
});
