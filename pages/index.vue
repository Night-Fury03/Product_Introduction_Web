<script setup>
import { ref, computed } from "vue";
import { ChevronLeftIcon, ChevronRightIcon } from "@heroicons/vue/24/outline";

const slides = [
    { image: "/19.jpg", title: "Slide 1", description: "Mô tả slide 1" },
    { image: "/29.jpg", title: "Slide 2", description: "Mô tả slide 2" },
    { image: "/51.jpg", title: "Slide 3", description: "Mô tả slide 3" },
    { image: "/009.jpg", title: "Slide 4", description: "Mô tả slide 3" },
    { image: "/49.jpg", title: "Slide 5", description: "Mô tả slide 3" },
];

const blogs = [
    { image: "/19.jpg", title: "Tiêu đề blog 1", text: "blog 1" },
    { image: "/29.jpg", title: "Tiêu đề blog 2", text: "blog 2" },
    { image: "/51.jpg", title: "Tiêu đề blog 3", text: "blog 3" },
]

const currentSlide = ref(0);
const transitioning = ref(false);

// Xoay vòng danh sách thumbnail
const rotatedSlides = computed(() => {
    const len = slides.length;
    return [
        slides[(currentSlide.value - 1 + len) % len], // Slide bên trái
        slides[currentSlide.value], // Slide chính giữa
        slides[(currentSlide.value + 1) % len], // Slide bên phải
    ];
});

const prevSlide = () => {
    currentSlide.value = (currentSlide.value - 1 + slides.length) % slides.length;
};

const nextSlide = () => {
    currentSlide.value = (currentSlide.value + 1) % slides.length;
};

// Dịch chuyển ảnh với hiệu ứng trơn tru
const goToSlide = (index) => {
    if (transitioning.value) return; // Ngăn spam click khi animation đang chạy
    transitioning.value = true;

    const diff = slides.indexOf(index) - currentSlide.value;
    if (diff === 0) return; // Nếu bấm vào ảnh giữa thì không cần làm gì

    // Tạo hiệu ứng trượt bằng cách thay đổi currentSlide sau khi animation hoàn tất
    setTimeout(() => {
        currentSlide.value = slides.indexOf(index);
        transitioning.value = false;
    }, 500); // Delay khớp với CSS transition
};

// Hiệu ứng dịch chuyển slide
const getSlideStyle = (index) => {
    return {
        transform: `translateX(${(index - 1) * 100}%) scale(${index === 1 ? 1.1 : 0.8})`,
        opacity: index === 1 ? 1 : 0.4,
        transition: "transform 0.5s ease-in-out, opacity 0.5s ease-in-out",
        zIndex: index === 1 ? 10 : 5,
    };
};
</script>


<template>
    <main>
        <!-- Slider -->
        <section class="bg-background relative">
            <div class="container flex flex-col lg:flex-row items-center py-20 gap-20">
                <!-- Product info -->
                <div class="flex-1 order-1 text-center lg:text-left">
                    <Transition name="fade-slide" mode="out-in">
                        <div :key="currentSlide">
                            <h1 class="text-4xl lg:text-6xl font-extrabold mb-6 text-balance">
                                {{ slides[currentSlide].title }}
                            </h1>
                            <p class="text-xl lg:text-2xl mb-8 text-balance text-text">
                                {{ slides[currentSlide].description }}
                            </p>
                            <button
                                class="relative overflow-hidden rounded-md h-12 px-2 border text-text group bg-white active:border-b-[2px] active:brightness-90 active:translate-y-[2px] transition-all">
                                <span class="relative z-20 transition-colors duration-500 group-hover:text-white">
                                    View Detail !
                                </span>

                                <span
                                    class="absolute -top-8 left-4 w-full h-full bg-secondary -translate-x-full group-hover:-translate-x-4 group-hover:translate-y-8 transition-transform duration-500">
                                    <span
                                        className="absolute right-3 bottom-3 translate-x-full translate-y-full z-10 w-6 h-6 rotate-45 bg-white group-hover:translate-x-full group-hover:-right-6 transition-transform duration-500"></span>
                                </span>
                            </button>
                        </div>
                    </Transition>
                </div>


                <!-- Product img -->
                <div
                    class="relative flex-1 lg:order-2 flex justify-center items-center w-full min-h-[250px] sm:min-h-[300px] lg:h-[300px] overflow-hidden">
                    <div v-for="(slide, index) in rotatedSlides" :key="slide.image" @click="goToSlide(slide)"
                        class="absolute cursor-pointer transition-all duration-500 ease-in-out bg-transparent p-4"
                        :style="getSlideStyle(index)">
                        <NuxtImg sizes="xs:100vw" format="webp" densities="x1" :src="slide.image" alt=""
                            class="object-cover rounded-lg h-[250px]" />
                    </div>
                </div>
            </div>

            <!-- Điều hướng -->
            <button @click="prevSlide"
                class="absolute top-[50%] translate-y-[-20px] left-4 hover:scale-110 hover:opacity-100 transition-all opacity-50">
                <ChevronLeftIcon class="h-10 text-text" />
            </button>
            <button @click="nextSlide"
                class="absolute top-[50%] translate-y-[-20px] right-4 hover:scale-110 hover:opacity-100 transition-all opacity-50">
                <ChevronRightIcon class="h-10 text-text" />
            </button>
        </section>

        <!-- New products -->
        <section class="container py-20">
            <h2 class="text-center text-3xl font-bold mb-6">New Products</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-8 gap-y-12">
                <div v-for="(slide, index) in slides" :key="index" class="flex flex-col shadow rounded-md">
                    <NuxtImg sizes="xs:100vw sm:356px" format="webp" densities="x1" :src="slide.image" alt=""
                        class="rounded-t-md" />
                    <div class="flex flex-col py-6 px-4 flex-1 gap-2">
                        <div class="flex justify-between items-center">
                            <h2 class="text-2xl font-medium">Toire</h2>
                            <h1 class="text-3xl font-bold">S001</h1>
                        </div>
                        <p class="text-xs font-light text-text opacity-80">680x390x430mm</p>
                        <p class="text-md font-light text-text">{{ slide.description }}</p>
                        <p class="text-md font-light text-text opacity-80">$30.00</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Hot blog -->
        <section class="bg-background py-20">
            <h2 class="text-center text-3xl font-bold mb-6">Hot Blog</h2>
            <div class="container flex flex-col gap-12">
                <div v-for="(blog, index) in blogs" :key="index" class="flex flex-col md:flex-row gap-6 items-center"
                    :class="index % 2 === 0 ? 'md:flex-row' : 'md:flex-row-reverse'">

                    <!-- Ảnh blog -->
                    <div class="flex-1 flex justify-center">
                        <NuxtImg format="webp" densities="x1" :src="blog.image" alt=""
                            class="rounded-md max-w-[356px] flex-1 shadow-md" />
                    </div>

                    <!-- Nội dung blog -->
                    <div class="flex-1" :class="index % 2 === 0 ? 'text-left' : 'text-right'">
                        <h3 class="text-2xl font-semibold mb-2">{{ blog.title }}</h3>
                        <p class="text-md font-light text-text">{{ blog.text }}</p>
                    </div>
                </div>
            </div>
        </section>
    </main>
</template>

<style>
/* Hiệu ứng trượt từ dưới lên */
.fade-slide-enter-active {
    transition: all 0.5s ease-out;
}

.fade-slide-leave-active {
    transition: all 0.3s ease-in;
}

.fade-slide-enter-from {
    opacity: 0;
    transform: translateY(50px);
}

.fade-slide-leave-to {
    opacity: 0;
    transform: translateY(-50px);
}
</style>
