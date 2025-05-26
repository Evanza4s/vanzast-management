import React from "react";
import HomeNavigation from "@/component/header/HomeNavigation";
import BackgroundHome from "@/assets/images/Background_dark_fantasy.jpg";
import Image from "next/image";
import { BodyContainer } from "@/component/container/BodyContainer";
import Link from "next/link";

const HomeClient = () => {
  return (
    <div className="@container">
      <div className="relative lg:min-h-screen">
        <Image
          src={BackgroundHome}
          alt="background home"
          className="absolute bg-center -z-10 contain-content"
          fill
          style={{ objectFit: "cover" }}
          quality={100}
        />
        <div className="absolute inset-0 bg-black opacity-35 -z-10" />
        <div className="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent -z-10" />
        <div className="absolute inset-0 bg-gradient-to-tl from-black via-transparent to-transparent -z-10" />
        <HomeNavigation />
        <BodyContainer className="px-4 sm:px-8 md:px-16 lg:px-24">
          <div className="flex flex-col md:flex-row justify-center md:justify-between w-full items-center md:mb-24 lg:mt-24">
            <div className="text-white max-w-xl w-full flex flex-col items-center md:items-start text-center md:text-left">
              <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold leading-tight">
                Explore A World Of{" "}
                <span className="bg-gradient-to-br from-amber-800 to-yellow-500 bg-clip-text text-transparent">
                  Mythical Story
                </span>
              </h1>
              <p className="mt-4 text-base sm:text-lg text-gray-300">
                Choose your class, write your story, forge your path, to save or
                conquer the Altera. Are you ready?
              </p>
              <div className="mt-6 flex flex-col sm:flex-row gap-4">
                <Link href="/">
                  <button className="px-6 py-2 bg-yellow-500 text-black rounded-lg">
                    Get Started
                  </button>
                </Link>
                <Link href="/">
                  <button className="px-6 py-2 border border-gray-300 text-white rounded-lg">
                    Login
                  </button>
                </Link>
              </div>
            </div>
            <div className="relative py-12 flex items-center justify-center w-full md:w-1/2">
              <h1>Right Side</h1>
            </div>
          </div>
        </BodyContainer>
      </div>
    </div>
  );
};

export default HomeClient;
