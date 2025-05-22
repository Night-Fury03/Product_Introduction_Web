<script setup>
import { ref, computed } from "vue";
import { ArrowUpRightIcon, ChevronLeftIcon, ChevronRightIcon } from "@heroicons/vue/24/outline";

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

const itemsPerPage = computed(() => {
    return process.client ? (window.innerWidth >= 1024 ? 4: 3) : 0;
    // if (window.innerWidth >= 1024) return 4; // Desktop
    // if (window.innerWidth >= 768) return 3;  // Tablet
    return 2; // Mobile
});


// Slider Recommended
const currentIndex = ref(0);
const recommendedItemsPerPage = 3;
const prev = () => currentIndex.value = Math.max(currentIndex.value - 1, 0);
const next = () => currentIndex.value = Math.min(currentIndex.value + 1, slides.length - recommendedItemsPerPage);

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

    if (Math.abs(diff) > 50) {
        if (diff > 0) {
            nextSlide();
        } else {
            prevSlide();
        }
    }
};

const featureTouchStartX = ref(0);
const featureTouchEndX = ref(0);

const onFeatureTouchStart = (event) => {
    featureTouchStartX.value = event.touches[0].clientX;
};

const onFeatureTouchMove = (event) => {
    featureTouchEndX.value = event.touches[0].clientX;
};

const onFeatureTouchEnd = () => {
    const diff = featureTouchStartX.value - featureTouchEndX.value;

    if (Math.abs(diff) > 50) {
        if (diff > 0) {
            next(); // Vuốt sang trái -> chuyển slide tiếp theo
        } else {
            prev(); // Vuốt sang phải -> chuyển slide trước đó
        }
    }
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
                <div class="relative flex-1 lg:order-2 flex justify-center items-center w-full min-h-[250px] sm:min-h-[300px] lg:h-[300px] overflow-hidden"
                    @touchstart="onTouchStart" @touchmove="onTouchMove" @touchend="onTouchEnd">
                    <NuxtLink v-for="(slide, index) in rotatedSlides" :key="slide.image" @click="goToSlide(slide)"
                        class="absolute cursor-pointer transition-all duration-500 ease-in-out bg-transparent p-4"
                        :style="getSlideStyle(index)">
                        <NuxtImg sizes="xs:100vw" format="webp" densities="x1" :src="slide.image" alt=""
                            class="object-cover rounded-lg h-[250px]" />
                    </NuxtLink>
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
        <section class="py-20">
            <h2 class="text-center text-3xl font-bold mb-6 autoShow">New Products</h2>
            <div class="container flex flex-col gap-12">
                <NuxtLink to="/details" v-for="(blog, index) in blogs" :key="index"
                    class="flex flex-col md:flex-row gap-6 items-center"
                    :class="index % 2 === 0 ? 'md:flex-row' : 'md:flex-row-reverse'">

                    <!-- Ảnh blog -->
                    <div class="flex-1 flex justify-center autoShow">
                        <NuxtImg format="webp" densities="x1" :src="blog.image" alt=""
                            class="rounded-md max-w-[356px] flex-1 shadow-md" />
                    </div>

                    <!-- Nội dung blog -->
                    <div class="flex-1 autoShow" :class="index % 2 === 0 ? 'text-left' : 'text-right'">
                        <h3 class="text-2xl font-semibold mb-2">{{ blog.title }}</h3>
                        <p class="text-md font-light text-text">{{ blog.text }}</p>
                    </div>
                </NuxtLink>
            </div>
        </section>

        <!-- feature products -->
        <section class="py-20">
            <div class="container flex justify-between items-center mb-12">
                <h2 class="text-center text-3xl font-bold fade-slide-left-to-right">Feature Products</h2>

                <div class="hidden md:block fade-slide-right-to-left">
                    <NuxtLink to="/products"
                        class="flex justify-center gap-6 items-center mx-auto backdrop-blur-md lg:font-semibold isolation-auto before:absolute before:w-full before:transition-all before:duration-700 before:hover:w-full before:-left-full before:hover:left-0 before:rounded-full before:bg-secondary hover:text-white before:-z-10 before:aspect-square before:hover:scale-150 before:hover:duration-700 relative z-10 px-4 py-1 overflow-hidden border border-border  rounded-full group">
                        <p class="text-base font-light ">Explore</p>
                        <ArrowUpRightIcon
                            class="w-8 h-8 justify-end group-hover:rotate-45 group-hover:bg-white group-hover:text-text ease-linear duration-300 rounded-full border border-border group-hover:border-none p-2 " />
                    </NuxtLink>
                </div>
            </div>

            <div class="relative flex items-center autoShow">
                <div class="relative overflow-hidden w-full pl-20 py-6" @touchstart="onFeatureTouchStart"
                    @touchmove="onFeatureTouchMove" @touchend="onFeatureTouchEnd">
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


                <button @click="prev"
                    class="absolute left-4  hover:scale-110 hover:opacity-100 transition-all opacity-50 z-10"
                    :disabled="currentIndex === 0">
                    <ChevronLeftIcon class="h-10 text-text" />
                </button>
                <button @click="next"
                    class="absolute right-4 hover:scale-110 hover:opacity-100 transition-all opacity-50 z-10"
                    :disabled="currentIndex >= slides.length - recommendedItemsPerPage">
                    <ChevronRightIcon class="h-10 text-text" />
                </button>
            </div>

            <div class="container block md:hidden mt-12 autoShow">
                <NuxtLink to="/blog"
                    class="w-1/2 flex justify-center gap-6 items-center mx-auto backdrop-blur-md lg:font-semibold isolation-auto before:absolute before:w-full before:transition-all before:duration-700 before:hover:w-full before:-left-full before:hover:left-0 before:rounded-full before:bg-secondary hover:text-white before:-z-10 before:aspect-square before:hover:scale-150 before:hover:duration-700 relative z-10 px-4 py-1 overflow-hidden border border-border  rounded-full group">
                    <p class="text-base font-light ">Explore</p>
                    <ArrowUpRightIcon
                        class="w-8 h-8 justify-end group-hover:rotate-45 group-hover:bg-white group-hover:text-text ease-linear duration-300 rounded-full border border-border group-hover:border-none p-2 " />
                </NuxtLink>
            </div>
        </section>

        <!-- Hot blog -->
        <section class="py-20">
            <div class="container flex justify-between items-center mb-12">
                <h2 class="text-center text-3xl font-bold fade-slide-left-to-right">Hot Blog</h2>

                <div class="hidden md:block fade-slide-right-to-left">
                    <NuxtLink to="/blog"
                        class="flex justify-center gap-6 items-center mx-auto backdrop-blur-md lg:font-semibold isolation-auto before:absolute before:w-full before:transition-all before:duration-700 before:hover:w-full before:-left-full before:hover:left-0 before:rounded-full before:bg-secondary hover:text-white before:-z-10 before:aspect-square before:hover:scale-150 before:hover:duration-700 relative z-10 px-4 py-1 overflow-hidden border border-border  rounded-full group">
                        <p class="text-base font-light ">Explore</p>
                        <ArrowUpRightIcon
                            class="w-8 h-8 justify-end group-hover:rotate-45 group-hover:bg-white group-hover:text-text ease-linear duration-300 rounded-full border border-border group-hover:border-none p-2 " />
                    </NuxtLink>
                </div>
            </div>
            <div class="container grid grid-cols-1 md:grid-cols-4 gap-12 ">
                <!-- Blog chính (Lớn) -->
                <div class="md:col-span-2 flex flex-col gap-6">
                    <NuxtImg format="webp" densities="x1" :src="blogs[0].image" alt=""
                        class="rounded-md w-full h-[250px] object-cover shadow-md fade-slide-left-to-right" />
                    <div class="fade-slide-left-to-right">
                        <h3 class="text-2xl font-semibold mb-2">{{ blogs[0].title }}</h3>
                        <p class="text-md font-light text-text">{{ blogs[0].text }}</p>
                    </div>
                </div>

                <!-- Danh sách các blog nhỏ -->
                <div class="md:col-span-2 flex flex-col gap-6">
                    <div v-for="(blog, index) in blogs.slice(1)" :key="index"
                        class="flex items-center gap-6 fade-slide-right-to-left">
                        <NuxtImg format="webp" densities="x1" :src="blog.image" alt=""
                            class="rounded-md w-1/2 h-20 object-cover shadow-md" />
                        <div>
                            <h4 class="text-lg font-semibold">{{ blog.title }} afasdvasvbasdv</h4>
                            <p class="text-sm text-text opacity-80">{{ blog.text }}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="container block md:hidden mt-12 autoShow">
                <NuxtLink to="/blog"
                    class="w-1/2 flex justify-center gap-6 items-center mx-auto backdrop-blur-md lg:font-semibold isolation-auto before:absolute before:w-full before:transition-all before:duration-700 before:hover:w-full before:-left-full before:hover:left-0 before:rounded-full before:bg-secondary hover:text-white before:-z-10 before:aspect-square before:hover:scale-150 before:hover:duration-700 relative z-10 px-4 py-1 overflow-hidden border border-border  rounded-full group">
                    <p class="text-base font-light ">Explore</p>
                    <ArrowUpRightIcon
                        class="w-8 h-8 justify-end group-hover:rotate-45 group-hover:bg-white group-hover:text-text ease-linear duration-300 rounded-full border border-border group-hover:border-none p-2 " />
                </NuxtLink>
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

.autoShow {
    animation: autoShowAnimation both;
    animation-timeline: view(70% 5%);
}

@keyframes autoShowAnimation {
    from {
        opacity: 0;
        transform: translateY(200px) scale(0.3);
    }

    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

.fade-slide-left-to-right {
    animation: leftToRightAnimation both;
    animation-timeline: view(70% 5%);
}

.fade-slide-right-to-left {
    animation: rightToLeftAnimation both;
    animation-timeline: view(70% 5%);
}

@keyframes leftToRightAnimation {
    from {
        clip-path: inset(0 100% 0 0);
        opacity: 0;
    }

    to {
        clip-path: inset(0 0 0 0);
        opacity: 1;
    }
}

@keyframes rightToLeftAnimation {
    from {
        clip-path: inset(0 0 0 100%);
        opacity: 0;
    }

    to {
        clip-path: inset(0 0 0 0);
        opacity: 1;
    }
}
</style>
