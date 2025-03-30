<script setup>

</script>
<template>
    <section class="py-20">
        <div class="container grid grid-cols-1 md:grid-cols-3 gap-4">
            <!-- main image -->
            <div class="md:col-span-2">
                <NuxtImg densities="x1" format="webp" src="../public/19.jpg" />
            </div>
            <!-- bonus image -->
            <div class="grid grid-cols-2 md:grid-cols-1 gap-4">
                <NuxtImg densities="x1" format="webp" src="../public/29.jpg" />
                <NuxtImg densities="x1" format="webp" src="../public/49.jpg" />
            </div>
        </div>

        <!-- details -->
        <div class="container mt-12">
            <!-- ID product -->
            <div class="flex items-center gap-2">
                <div class="text-end">
                    <p class="text-lg">Model</p>
                    <h2 class="text-2xl font-bold">Model</h2>
                </div>

                <div class="h-[50px] w-[1px] bg-border"></div>

                <div class="">
                    <h1 class="text-5xl font-black">S580</h1>
                </div>
            </div>

            <!-- Name, size ... -->
            <div class="py-8 flex flex-col md:flex-row gap-8">
                <div class="flex flex-col gap-2 flex-1">
                    <p class="text-lg">Name: Toire</p>
                    <p class="text-lg">Dimensions: 710x410x470mm</p>
                    <p class="text-lg">Pit distance: 300/400mm</p>
                    <p class="text-base">Heating: running water instant heating</p>
                </div>

                <div class="flex flex-col gap-2 flex-1">
                    <p class="text-lg font-bold">Feature</p>
                    <p class="text-base">Hightlight:</p>
                    <div class="flex gap-8">
                        <div class="flex flex-col gap-1 items-center">
                            <div class="w-12 h-12 rounded-full bg-background"></div>
                            <p class="text-sm text-text">colorful</p>
                        </div>
                        <div class="flex flex-col gap-1 items-center">
                            <div class="w-12 h-12 rounded-full bg-background"></div>
                            <p class="text-sm text-text">colorful</p>
                        </div>
                        <div class="flex flex-col gap-1 items-center">
                            <div class="w-12 h-12 rounded-full bg-background"></div>
                            <p class="text-sm text-text">colorful</p>
                        </div>
                        <div class="flex flex-col gap-1 items-center">
                            <div class="w-12 h-12 rounded-full bg-background"></div>
                            <p class="text-sm text-text">colorful</p>
                        </div>
                    </div>
                </div>
            </div>

            <!--  -->
            <div class="py-8 grid lg:grid-cols-9 gap-8">
                <div class="lg:col-span-6 grid grid-cols-3 gap-4">
                    <p class="col-span-3 text-lg font-bold">Optional configuration: without water tank / with water tank
                    </p>
                    <div class="p-8 text-center border border-border rounded-xl">
                        <h1 class="font-bold text-2xl">Standard version</h1>
                        <p class="font-medium text-lg">Manual clip cover</p>
                        <p class="text-base">Foot touch flush</p>
                    </div>
                    <div class="p-8 text-center border border-border rounded-xl">
                        <h1 class="font-bold text-2xl">Standard version</h1>
                        <p class="font-medium text-lg">Manual clip cover</p>
                        <p class="text-base">Foot touch flush</p>
                    </div>
                    <div class="p-8 text-center border border-border rounded-xl">
                        <h1 class="font-bold text-2xl">Standard version</h1>
                        <p class="font-medium text-lg">Manual clip cover</p>
                        <p class="text-base">Foot touch flush</p>
                    </div>
                </div>

                <!-- color -->
                <div class="lg:col-span-3 grid grid-cols-4 lg:grid-cols-2 gap-4">
                    <div class="relative">
                        <div class="w-24 h-24 bg-background"></div>
                        <p class="absolute top-0 right-0 text-sm text-text">green</p>
                    </div>
                    <div class="relative">
                        <div class="w-24 h-24 bg-background"></div>
                        <p class="absolute top-0 right-0 text-sm text-text">green</p>
                    </div>
                    <div class="relative">
                        <div class="w-24 h-24 bg-background"></div>
                        <p class="absolute top-0 right-0 text-sm text-text">green</p>
                    </div>
                    <div class="relative">
                        <div class="w-24 h-24 bg-background"></div>
                        <p class="absolute top-0 right-0 text-sm text-text">green</p>
                    </div>
                </div>
            </div>

            <!-- description -->
            <div class="py-8 flex flex-col gap-4">
                <p class="text-lg font-bold">Basic</p>
                <p class="text-base">A toilet is a piece of sanitary hardware that collects human waste (urine and
                    feces), and sometimes toilet paper, usually for disposal. Flush toilets use water, while dry or
                    non-flush toilets do not.</p>
            </div>
        </div>
    </section>
</template>