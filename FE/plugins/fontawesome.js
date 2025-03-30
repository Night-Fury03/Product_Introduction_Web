import { library } from "@fortawesome/fontawesome-svg-core";
import { faFacebook, faTwitter, faInstagram } from "@fortawesome/free-brands-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faMagnifyingGlass } from '@fortawesome/free-solid-svg-icons'

// Thêm icon vào thư viện
library.add(faFacebook, faTwitter, faInstagram, faMagnifyingGlass);

export default defineNuxtPlugin((nuxtApp) => {
    nuxtApp.vueApp.component("font-awesome-icon", FontAwesomeIcon);
});
