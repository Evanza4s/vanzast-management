import React from "react";
import { BodyContainer } from "@/component/container/BodyContainer";
import BackgroundNews from "@/assets/images/Background_tample.jpg";
import Image from "next/image";

const NewsSection = () => {
  return (
    <div className="@container">
      <div className="relative lg:min-h-screen">
        <Image
          src={BackgroundNews}
          alt="background home"
          className="absolute bg-center -z-10 contain-content"
          fill
          style={{ objectFit: "cover" }}
          quality={100}
        />
        <div className="absolute inset-0 bg-black opacity-40 -z-10" />
        <div className="absolute inset-0 bg-gradient-to-b from-black via-transparent to-transparent -z-10" />
        <BodyContainer className="px-4 sm:px-8 md:px-16 lg:px-24 pt-24 md:pt-32 overflow-hidden z-30">
          <div className="flex w-full items-center justify-center">
            
          </div>
        </BodyContainer>
      </div>
    </div>
  );
};

export default NewsSection;
