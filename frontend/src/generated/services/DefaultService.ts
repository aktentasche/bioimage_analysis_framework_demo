/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Body_detect_ridges_detect_ridges_post } from '../models/Body_detect_ridges_detect_ridges_post';
import type { Body_isolate_rgb_isolate_rgb_post } from '../models/Body_isolate_rgb_isolate_rgb_post';
import type { Body_recognize_faces_recognize_faces_post } from '../models/Body_recognize_faces_recognize_faces_post';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class DefaultService {

    /**
     * Detect Ridges
     * @param formData
     * @returns any Successful Response
     * @throws ApiError
     */
    public static detectRidgesDetectRidgesPost(
        formData: Body_detect_ridges_detect_ridges_post,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/detect_ridges',
            formData: formData,
            mediaType: 'multipart/form-data',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Isolate Rgb
     * @param formData
     * @returns any Successful Response
     * @throws ApiError
     */
    public static isolateRgbIsolateRgbPost(
        formData: Body_isolate_rgb_isolate_rgb_post,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/isolate_rgb',
            formData: formData,
            mediaType: 'multipart/form-data',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Recognize Faces
     * @param formData
     * @returns any Successful Response
     * @throws ApiError
     */
    public static recognizeFacesRecognizeFacesPost(
        formData: Body_recognize_faces_recognize_faces_post,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/recognize_faces',
            formData: formData,
            mediaType: 'multipart/form-data',
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
