<script setup>
import { ref, computed } from "vue";
import {
    ArchiveBoxIcon, HomeIcon, MusicalNoteIcon, DevicePhoneMobileIcon, ServerStackIcon, ChevronRightIcon, ChevronLeftIcon
} from "@heroicons/vue/24/outline";

// tất cả sản phẩm lấy từ dữ liệu
const slides = [
    { image: "/19.jpg", title: "Slide 1", description: "Mô tả slide 1" },
    { image: "/29.jpg", title: "Slide 2", description: "Mô tả slide 2" },
    { image: "/51.jpg", title: "Slide 3", description: "Mô tả slide 3" },
    { image: "/009.jpg", title: "Slide 4", description: "Mô tả slide 3" },
    { image: "/49.jpg", title: "Slide 5", description: "Mô tả slide 3" },
    { image: "/19.jpg", title: "Slide 1", description: "Mô tả slide 1" },
    { image: "/29.jpg", title: "Slide 2", description: "Mô tả slide 2" },
    { image: "/51.jpg", title: "Slide 3", description: "Mô tả slide 3" },
    { image: "/009.jpg", title: "Slide 4", description: "Mô tả slide 3" },
    { image: "/49.jpg", title: "Slide 5", description: "Mô tả slide 3" },
];

const categories = ref([
    { name: "All Product", icon: ArchiveBoxIcon, open: false, subCategories: [] },
    { name: "For Home", icon: HomeIcon, open: false, subCategories: ["Living Room", "Kitchen", "Bedroom"] },
    { name: "For Music", icon: MusicalNoteIcon, open: false, subCategories: ["Headphones", "Speakers"] },
    { name: "For Phone", icon: DevicePhoneMobileIcon, open: false, subCategories: ["Accessories", "Cases"] },
    { name: "For Storage", icon: ServerStackIcon, open: false, subCategories: ["SSD", "HDD", "USB"] },
]);

const activeIndex = ref(null);

// Hàm toggle mở danh mục con (chỉ mở một danh mục tại một thời điểm)
const toggleCategory = (index) => {
    activeIndex.value = activeIndex.value === index ? null : index;
};

// Phân trang
const itemsPerPage = 3;
const currentPage = ref(1);
const totalPages = computed(() => Math.ceil(slides.length / itemsPerPage));
const paginatedSlides = computed(() => slides.slice((currentPage.value - 1) * itemsPerPage, currentPage.value * itemsPerPage));
const prevPage = () => currentPage.value > 1 && currentPage.value--;
const nextPage = () => currentPage.value < totalPages.value && currentPage.value++;

// Slider Recommended
const currentIndex = ref(0);
const recommendedItemsPerPage = 3;
const prevSlide = () => currentIndex.value = Math.max(currentIndex.value - 1, 0);
const nextSlide = () => currentIndex.value = Math.min(currentIndex.value + 1, slides.length - recommendedItemsPerPage);

const touchStartX = ref(0);
const touchEndX = ref(0);

const onTouchStart = (event) => {
    touchStartX.value = event.touches[0].clientX;
};

const onTouchMove = (event) => {
    touchEndX.value = event.touches[0].clientX;
};

const onTouchEnd = () => {
    const diff = touchStartX.value - touchEndX.value;

    if (diff > 50) {
        // Vuốt trái (Next slide)
        nextSlide();
    } else if (diff < -50) {
        // Vuốt phải (Previous slide)
        prevSlide();
    }
};

</script>
<template>
    <main>
        <section class="bg-primary">
            <!-- search bar -->
            <div
                class="container flex flex-col lg:flex-row gap-10 justify-center lg:justify-between items-center px-4 pb-16 h-[300px]">
                <div class="lg:flex-1">
                    <h1 class="text-3xl font-bold text-white">Give All You Need</h1>
                </div>

                <div class="lg:flex-1 flex justify-center items-center border rounded-full py-2 px-4 w-full">
                    <font-awesome-icon icon="magnifying-glass" class="text-white opacity-50" />
                    <input placeholder="search..." type="text"
                        class="outline-none text-base text-text bg-transparent w-full font-normal px-4" />
                </div>
            </div>
        </section>


        <section
            class="container py-20 grid grid-cols-1 md:grid-cols-4 lg:grid-cols-12 gap-8 relative bg-white -top-16 rounded-t-2xl">
            <!-- categories -->
            <div class="md:col-span-1 lg:col-span-3 flex flex-col gap-y-8">
                <h2 class="text-2xl font-semibold mb-4">Category</h2>

                <!-- Danh mục chính -->
                <ul class="space-y-2">
                    <li v-for="(category, index) in categories" :key="index">
                        <div class="flex items-center justify-between text-gray-700 cursor-pointer p-2 hover:bg-gray-100 rounded-md"
                            @click="toggleCategory(index)">
                            <div class="flex items-center gap-3">
                                <component :is="category.icon" class="h-5 w-5 text-gray-600" />
                                <span class="text-sm">{{ category.name }}</span>
                            </div>

                            <!-- Mũi tên xoay khi mở -->
                            <ChevronRightIcon class="h-5 w-5 text-gray-500 transition-transform duration-300"
                                :class="{ 'rotate-90': activeIndex === index }" />
                        </div>

                        <!-- Danh mục con (Hiệu ứng dropdown mượt mà) -->
                        <transition name="dropdown">
                            <ul v-if="activeIndex === index" class="pl-8 mt-1 space-y-2 cursor-pointer">
                                <li v-for="(sub, subIndex) in category.subCategories" :key="subIndex"
                                    class="flex items-center gap-3 text-gray-600 hover:text-secondary">
                                    <span class="text-xs">{{ sub }}</span>
                                </li>
                            </ul>
                        </transition>
                    </li>
                </ul>
            </div>

            <!-- list products -->
            <div class="md:col-span-3 lg:col-span-9 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div v-for="slide in paginatedSlides" :key="slide.image"
                    class="col-span-1 flex flex-col shadow rounded-md">
                    <NuxtImg :src="slide.image" alt="" class="rounded-t-md w-full" />
                    <div class="flex flex-col py-6 px-4 flex-1 gap-2">
                        <h2 class="text-2xl font-medium">Toire</h2>
                        <p class="text-md font-light">{{ slide.description }}</p>
                        <p class="text-md font-light opacity-80">$30.00</p>
                    </div>
                </div>

                <!-- Pagination Controls -->
                <div class="md:col-span-2 lg:col-span-3 flex justify-between items-center gap-4 mt-8">
                    <button @click="prevPage" :disabled="currentPage === 1"
                        class="px-4 py-2 text-white bg-gray-700 rounded-lg disabled:opacity-30 active:border-b-[2px] active:brightness-90 active:translate-y-[2px] transition-all">
                        Previous
                    </button>

                    <span class="text-lg font-thin text-text">{{ currentPage }} / {{ totalPages }}</span>

                    <button @click="nextPage" :disabled="currentPage === totalPages"
                        class="px-4 py-2 text-white bg-gray-700 rounded-lg disabled:opacity-30 active:border-b-[2px] active:brightness-90 active:translate-y-[2px] transition-all">
                        Next
                    </button>
                </div>
            </div>
        </section>

        <!-- Recommended Slider -->
        <section class="py-12">
            <div class="container">
                <h1 class="text-3xl font-bold mb-6">Recommended</h1>
            </div>

            <div class="relative flex items-center">
                <div class="relative overflow-hidden w-full pl-20 py-6" @touchstart="onTouchStart"
                    @touchmove="onTouchMove" @touchend="onTouchEnd">
                    <div class="flex gap-6 transition-transform duration-300 ease-in-out"
                        :style="{ transform: `translateX(-${currentIndex * (100 / itemsPerPage)}%)` }">
                        <div v-for="(slide, index) in slides" :key="index"
                            class="min-w-[calc(100%/4)] bg-white shadow-md rounded-lg overflow-hidden">
                            <NuxtImg :src="slide.image" alt="" class="w-full h-48 object-cover" />
                            <div class="p-4">
                                <h2 class="text-lg font-semibold mt-2">{{ slide.title }}</h2>
                                <p class="text-lg font-bold mt-2">{{ slide.price }}</p>
                            </div>
                        </div>
                    </div>
                </div>


                <button @click="prevSlide"
                    class="absolute left-0  hover:bg-background p-2 rounded-full hover:shadow-lg z-10"
                    :disabled="currentIndex === 0">
                    <ChevronLeftIcon class="w-6 h-6" />
                </button>
                <button @click="nextSlide"
                    class="absolute right-0 hover:bg-background p-2 rounded-full hover:shadow-lg z-10"
                    :disabled="currentIndex >= slides.length - recommendedItemsPerPage">
                    <ChevronRightIcon class="w-6 h-6" />
                </button>
            </div>
        </section>
    </main>
</template>

<style>
.dropdown-enter-active,
.dropdown-leave-active {
    transition: max-height 0.3s ease-in-out, opacity 0.3s ease-in-out;
}

.dropdown-enter-from,
.dropdown-leave-to {
    max-height: 0;
    opacity: 0;
}

.dropdown-enter-to,
.dropdown-leave-from {
    max-height: 100px;
    opacity: 1;
}
</style>