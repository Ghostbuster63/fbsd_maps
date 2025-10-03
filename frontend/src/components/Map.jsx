"use client";

import { useState } from "react";
//import { RedPin, BluePin, GrnPin, YelPin } from "./Pins";
import { RedPoints, BluePoints, YelPoints, GrnPoints, OrgPoints } from "./Points";
import config from "../data/config.json";

import {
  APIProvider,
  Map,
  useMap,
  AdvancedMarker,
  InfoWindow,
} from "@vis.gl/react-google-maps";


//export function Intro() {
export const MapComp = () => {
  const center = { lat: 50.52088296701928, lng: -110.21465690222468 };
  const zoom = 18;

  const MapTypeId = {
    HYBRID: 'hybrid',
    ROADMAP: 'roadmap',
    SATELLITE: 'satellite',
    TERRAIN: 'terrain'
  };

  const mapConf = {
    id: 'satellite',
    label: 'Satellite ("light" mapId)',
    mapId: '49ae42fed52588c3',
    mapTypeId: MapTypeId.SATELLITE
  };

  return (
    <>
    <h3>
      Canola 2025
    </h3>
    <APIProvider
      apiKey={config.MAP_API_KEY}
      onLoad={() => console.log('Intro API has loaded.')}
    >
      <div style={{ height: "95vh", width: "95%", overflow:"visible" }}>
        <Map 
          defaultZoom={zoom}
          defaultCenter={center}
          mapId={'ADE'}
          styling={'overflow: visible'}
          mapTypeId={mapConf.mapTypeId}
         >
          <RedPoints zoom={zoom} />
          <BluePoints zoom={zoom} />
          <YelPoints zoom={zoom} />
          <GrnPoints zoom={zoom} />
          <OrgPoints zoom={zoom} />
        </Map>
      </div>
    </APIProvider>
    </>
  );
}
