// GeolocationMarker.jsx
// https://github.com/visgl/react-google-maps/discussions/552
import React, { useEffect, useMemo } from "react";
import { useMap } from "@vis.gl/react-google-maps";

const GeolocationMarker = ({ position, accuracy }) => {
  const map = useMap();

  const geolocationMarker = useMemo(() => {
    if (!map) return null;

    const marker = new google.maps.Marker({
      position,
      map,
      icon: {
        path: google.maps.SymbolPath.CIRCLE,
        fillColor: "#4285F4",
        fillOpacity: 1,
        scale: 8,
        strokeColor: "#FFFFFF",
        strokeWeight: 2,
      },
    });

    return { marker };
  }, [map, position]);

  const accuracyCircle = useMemo(() => {
    if (!map || !position) return null;

    return new google.maps.Circle({
      strokeColor: "#4285F4",
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: "#4285F4",
      fillOpacity: 0.35,
      map,
      center: position,
      radius: accuracy,
    });
  }, [map, position, accuracy]);

  useEffect(() => {
    if (geolocationMarker) {
      geolocationMarker.marker.setMap(map);
    }
    if (accuracyCircle) {
      accuracyCircle.setMap(map);
    }

    return () => {
      if (geolocationMarker) {
        geolocationMarker.marker.setMap(null);
      }
      if (accuracyCircle) {
        accuracyCircle.setMap(null);
      }
    };
  }, [geolocationMarker, accuracyCircle, map]);

  return null; 
};

export default GeolocationMarker;
