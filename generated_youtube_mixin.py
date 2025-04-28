"""File generated with:
/home/celelibi/code/youtube-interactions/gen_youtube_api.py
generated_youtube_mixin.py"""

class YouTubeMixin:
    # pylint: disable=too-many-public-methods,too-many-lines
    """YouTube Data API v3

    The YouTube Data API v3 is an API that provides access to YouTube data,
    such as videos, playlists, and channels."""

    def abuse_reports_insert(self, part, request_args=None, **kwargs):
        """Inserts a new resource into this collection.

        Required arguments:
        - part: string: The *part* parameter serves two purposes in this
          operation. It identifies the properties that the write operation
          will set as well as the properties that the API response will include.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        return self.post('abuseReports', params=kwargs, **request_args)



    def activities_list(self, part, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Required arguments:
        - part: string: The *part* parameter specifies a comma-separated list
          of one or more activity resource properties that the API response
          will include. If the parameter identifies a property that contains
          child properties, the child properties will be included in the
          response. For example, in an activity resource, the snippet property
          contains other properties that identify the type of activity, a
          display title for the activity, and so forth. If you set
          *part=snippet*, the API response will also contain all of those
          nested properties.

        Optional arguments:
        - channel_id: string
        - home: boolean
        - max_results: integer: The *maxResults* parameter specifies the
          maximum number of items that should be returned in the result set.
        - mine: boolean
        - page_token: string: The *pageToken* parameter identifies a specific
          page in the result set that should be returned. In an API response,
          the nextPageToken and prevPageToken properties identify other pages
          that could be retrieved.
        - published_after: string
        - published_before: string
        - region_code: string
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'channel_id': 'channelId',
            'max_results': 'maxResults',
            'page_token': 'pageToken',
            'published_after': 'publishedAfter',
            'published_before': 'publishedBefore',
            'region_code': 'regionCode',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('activities', params=kwargs, **request_args)



    def captions_delete(self, id_, request_args=None, **kwargs):
        """Deletes a resource.

        Required arguments:
        - id_: string

        Optional arguments:
        - on_behalf_of: string: ID of the Google+ Page for the channel that
          the request is be on behalf of
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The actual CMS account that the user
          authenticates with must be linked to the specified YouTube content
          owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'id_': id_})
        style_conv = {
            'id_': 'id',
            'on_behalf_of': 'onBehalfOf',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.delete('captions', params=kwargs, **request_args)



    def captions_download(self, id_, request_args=None, **kwargs):
        """Downloads a caption track.

        Required arguments:
        - id_: string: The ID of the caption track to download, required for
          One Platform.

        Optional arguments:
        - on_behalf_of: string: ID of the Google+ Page for the channel that
          the request is be on behalf of
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The actual CMS account that the user
          authenticates with must be linked to the specified YouTube content
          owner.
        - tfmt: string: Convert the captions into this format. Supported
          options are sbv, srt, and vtt.
        - tlang: string: tlang is the language code; machine translate the
          captions into this language.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'id_': id_})
        style_conv = {
            'id_': 'id',
            'on_behalf_of': 'onBehalfOf',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        # pylint: disable=consider-using-f-string
        path = 'captions/{id}'.format(**kwargs)
        return self.get(path, params=kwargs)



    def captions_insert(self, part, request_args=None, **kwargs):
        """Inserts a new resource into this collection.

        Required arguments:
        - part: string: The *part* parameter specifies the caption resource
          parts that the API response will include. Set the parameter value to
          snippet.

        Optional arguments:
        - on_behalf_of: string: ID of the Google+ Page for the channel that
          the request is be on behalf of
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The actual CMS account that the user
          authenticates with must be linked to the specified YouTube content
          owner.
        - sync: boolean: Extra parameter to allow automatically syncing the
          uploaded caption/transcript with the audio.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'on_behalf_of': 'onBehalfOf',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('captions', params=kwargs, **request_args)



    def captions_list(self, part, video_id, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Required arguments:
        - part: string: The *part* parameter specifies a comma-separated list
          of one or more caption resource parts that the API response will
          include. The part names that you can include in the parameter value
          are id and snippet.
        - video_id: string: Returns the captions for the specified video.

        Optional arguments:
        - id_: string: Returns the captions with the given IDs for Stubby or
          Apiary.
        - on_behalf_of: string: ID of the Google+ Page for the channel that
          the request is on behalf of.
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The actual CMS account that the user
          authenticates with must be linked to the specified YouTube content
          owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part, 'video_id': video_id})
        style_conv = {
            'id_': 'id',
            'on_behalf_of': 'onBehalfOf',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'video_id': 'videoId',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('captions', params=kwargs, **request_args)



    def captions_update(self, part, request_args=None, **kwargs):
        """Updates an existing resource.

        Required arguments:
        - part: string: The *part* parameter specifies a comma-separated list
          of one or more caption resource parts that the API response will
          include. The part names that you can include in the parameter value
          are id and snippet.

        Optional arguments:
        - on_behalf_of: string: ID of the Google+ Page for the channel that
          the request is on behalf of.
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The actual CMS account that the user
          authenticates with must be linked to the specified YouTube content
          owner.
        - sync: boolean: Extra parameter to allow automatically syncing the
          uploaded caption/transcript with the audio.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'on_behalf_of': 'onBehalfOf',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.put('captions', params=kwargs, **request_args)



    def channel_banners_insert(self, request_args=None, **kwargs):
        """Inserts a new resource into this collection.

        Optional arguments:
        - channel_id: string: Unused, channel_id is currently derived from the
          security context of the requestor.
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The actual CMS account that the user
          authenticates with must be linked to the specified YouTube content
          owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({})
        style_conv = {
            'channel_id': 'channelId',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('channelBanners/insert', params=kwargs, **request_args)



    def channel_sections_delete(self, id_, request_args=None, **kwargs):
        """Deletes a resource.

        Required arguments:
        - id_: string

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'id_': id_})
        style_conv = {
            'id_': 'id',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.delete('channelSections', params=kwargs, **request_args)



    def channel_sections_insert(self, part, request_args=None, **kwargs):
        """Inserts a new resource into this collection.

        Required arguments:
        - part: string: The *part* parameter serves two purposes in this
          operation. It identifies the properties that the write operation
          will set as well as the properties that the API response will
          include. The part names that you can include in the parameter value
          are snippet and contentDetails.

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('channelSections', params=kwargs, **request_args)



    def channel_sections_list(self, part, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Required arguments:
        - part: string: The *part* parameter specifies a comma-separated list
          of one or more channelSection resource properties that the API
          response will include. The part names that you can include in the
          parameter value are id, snippet, and contentDetails. If the
          parameter identifies a property that contains child properties, the
          child properties will be included in the response. For example, in a
          channelSection resource, the snippet property contains other
          properties, such as a display title for the channelSection. If you
          set *part=snippet*, the API response will also contain all of those
          nested properties.

        Optional arguments:
        - channel_id: string: Return the ChannelSections owned by the
          specified channel ID.
        - hl: string: Return content in specified language
        - id_: string: Return the ChannelSections with the given IDs for
          Stubby or Apiary.
        - mine: boolean: Return the ChannelSections owned by the authenticated
          user.
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'channel_id': 'channelId',
            'id_': 'id',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('channelSections', params=kwargs, **request_args)



    def channel_sections_update(self, part, request_args=None, **kwargs):
        """Updates an existing resource.

        Required arguments:
        - part: string: The *part* parameter serves two purposes in this
          operation. It identifies the properties that the write operation
          will set as well as the properties that the API response will
          include. The part names that you can include in the parameter value
          are snippet and contentDetails.

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.put('channelSections', params=kwargs, **request_args)



    def channels_list(self, part, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Required arguments:
        - part: string: The *part* parameter specifies a comma-separated list
          of one or more channel resource properties that the API response
          will include. If the parameter identifies a property that contains
          child properties, the child properties will be included in the
          response. For example, in a channel resource, the contentDetails
          property contains other properties, such as the uploads properties.
          As such, if you set *part=contentDetails*, the API response will
          also contain all of those nested properties.

        Optional arguments:
        - category_id: string: Return the channels within the specified guide
          category ID.
        - for_handle: string: Return the channel associated with a YouTube
          handle.
        - for_username: string: Return the channel associated with a YouTube
          username.
        - hl: string: Stands for "host language". Specifies the localization
          language of the metadata to be filled into snippet.localized. The
          field is filled with the default metadata if there is no
          localization in the specified language. The parameter value must be
          a language code included in the list returned by the
          i18nLanguages.list method (e.g. en_US, es_MX).
        - id_: string: Return the channels with the specified IDs.
        - managed_by_me: boolean: Return the channels managed by the
          authenticated user.
        - max_results: integer: The *maxResults* parameter specifies the
          maximum number of items that should be returned in the result set.
        - mine: boolean: Return the ids of channels owned by the authenticated
          user.
        - my_subscribers: boolean: Return the channels subscribed to the
          authenticated user
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - page_token: string: The *pageToken* parameter identifies a specific
          page in the result set that should be returned. In an API response,
          the nextPageToken and prevPageToken properties identify other pages
          that could be retrieved.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'category_id': 'categoryId',
            'for_handle': 'forHandle',
            'for_username': 'forUsername',
            'id_': 'id',
            'managed_by_me': 'managedByMe',
            'max_results': 'maxResults',
            'my_subscribers': 'mySubscribers',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'page_token': 'pageToken',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('channels', params=kwargs, **request_args)



    def channels_update(self, part, request_args=None, **kwargs):
        """Updates an existing resource.

        Required arguments:
        - part: string: The *part* parameter serves two purposes in this
          operation. It identifies the properties that the write operation
          will set as well as the properties that the API response will
          include. The API currently only allows the parameter value to be set
          to either brandingSettings or invideoPromotion. (You cannot update
          both of those parts with a single request.) Note that this method
          overrides the existing values for all of the mutable properties that
          are contained in any parts that the parameter value specifies.

        Optional arguments:
        - on_behalf_of_content_owner: string: The *onBehalfOfContentOwner*
          parameter indicates that the authenticated user is acting on behalf
          of the content owner specified in the parameter value. This
          parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The actual CMS account that the user
          authenticates with needs to be linked to the specified YouTube
          content owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.put('channels', params=kwargs, **request_args)



    def comment_threads_insert(self, part, request_args=None, **kwargs):
        """Inserts a new resource into this collection.

        Required arguments:
        - part: string: The *part* parameter identifies the properties that
          the API response will include. Set the parameter value to snippet.
          The snippet part has a quota cost of 2 units.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        return self.post('commentThreads', params=kwargs, **request_args)



    def comment_threads_list(self, part, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Required arguments:
        - part: string: The *part* parameter specifies a comma-separated list
          of one or more commentThread resource properties that the API
          response will include.

        Optional arguments:
        - all_threads_related_to_channel_id: string: Returns the comment
          threads of all videos of the channel and the channel comments as well.
        - channel_id: string: Returns the comment threads for all the channel
          comments (ie does not include comments left on videos).
        - id_: string: Returns the comment threads with the given IDs for
          Stubby or Apiary.
        - max_results: integer: The *maxResults* parameter specifies the
          maximum number of items that should be returned in the result set.
        - moderation_status: string: Limits the returned comment threads to
          those with the specified moderation status. Not compatible with the
          'id' filter. Valid values: published, heldForReview, likelySpam.
        - order: string
        - page_token: string: The *pageToken* parameter identifies a specific
          page in the result set that should be returned. In an API response,
          the nextPageToken and prevPageToken properties identify other pages
          that could be retrieved.
        - post_id: string: Returns the comment threads of the specified post.
        - search_terms: string: Limits the returned comment threads to those
          matching the specified key words. Not compatible with the 'id' filter.
        - text_format: string: The requested text format for the returned
          comments.
        - video_id: string: Returns the comment threads of the specified video.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'all_threads_related_to_channel_id': 'allThreadsRelatedToChannelId',
            'channel_id': 'channelId',
            'id_': 'id',
            'max_results': 'maxResults',
            'moderation_status': 'moderationStatus',
            'page_token': 'pageToken',
            'post_id': 'postId',
            'search_terms': 'searchTerms',
            'text_format': 'textFormat',
            'video_id': 'videoId',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('commentThreads', params=kwargs, **request_args)



    def comments_delete(self, id_, request_args=None, **kwargs):
        """Deletes a resource.

        Required arguments:
        - id_: string
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'id_': id_})
        style_conv = {
            'id_': 'id',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.delete('comments', params=kwargs, **request_args)



    def comments_insert(self, part, request_args=None, **kwargs):
        """Inserts a new resource into this collection.

        Required arguments:
        - part: string: The *part* parameter identifies the properties that
          the API response will include. Set the parameter value to snippet.
          The snippet part has a quota cost of 2 units.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        return self.post('comments', params=kwargs, **request_args)



    def comments_list(self, part, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Required arguments:
        - part: string: The *part* parameter specifies a comma-separated list
          of one or more comment resource properties that the API response
          will include.

        Optional arguments:
        - id_: string: Returns the comments with the given IDs for One Platform.
        - max_results: integer: The *maxResults* parameter specifies the
          maximum number of items that should be returned in the result set.
        - page_token: string: The *pageToken* parameter identifies a specific
          page in the result set that should be returned. In an API response,
          the nextPageToken and prevPageToken properties identify other pages
          that could be retrieved.
        - parent_id: string: Returns replies to the specified comment. Note,
          currently YouTube features only one level of replies (ie replies to
          top level comments). However replies to replies may be supported in
          the future.
        - text_format: string: The requested text format for the returned
          comments.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'id_': 'id',
            'max_results': 'maxResults',
            'page_token': 'pageToken',
            'parent_id': 'parentId',
            'text_format': 'textFormat',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('comments', params=kwargs, **request_args)



    def comments_mark_as_spam(self, id_, request_args=None, **kwargs):
        """Expresses the caller's opinion that one or more comments should be
        flagged as spam.

        Required arguments:
        - id_: string: Flags the comments with the given IDs as spam in the
          caller's opinion.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'id_': id_})
        style_conv = {
            'id_': 'id',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('comments/markAsSpam', params=kwargs, **request_args)



    def comments_set_moderation_status(self, id_, moderation_status, request_args=None, **kwargs):
        """Sets the moderation status of one or more comments.

        Required arguments:
        - id_: string: Modifies the moderation status of the comments with the
          given IDs
        - moderation_status: string: Specifies the requested moderation
          status. Note, comments can be in statuses, which are not available
          through this call. For example, this call does not allow to mark a
          comment as 'likely spam'. Valid values: 'heldForReview', 'published'
          or 'rejected'.

        Optional arguments:
        - ban_author: boolean: If set to true the author of the comment gets
          added to the ban list. This means all future comments of the author
          will autmomatically be rejected. Only valid in combination with
          STATUS_REJECTED.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'id_': id_, 'moderation_status': moderation_status})
        style_conv = {
            'ban_author': 'banAuthor',
            'id_': 'id',
            'moderation_status': 'moderationStatus',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('comments/setModerationStatus', params=kwargs, **request_args)



    def comments_update(self, part, request_args=None, **kwargs):
        """Updates an existing resource.

        Required arguments:
        - part: string: The *part* parameter identifies the properties that
          the API response will include. You must at least include the snippet
          part in the parameter value since that part contains all of the
          properties that the API request can update.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        return self.put('comments', params=kwargs, **request_args)



    def i18n_languages_list(self, part, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Required arguments:
        - part: string: The *part* parameter specifies the i18nLanguage
          resource properties that the API response will include. Set the
          parameter value to snippet.

        Optional arguments:
        - hl: string
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        return self.get('i18nLanguages', params=kwargs, **request_args)



    def i18n_regions_list(self, part, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Required arguments:
        - part: string: The *part* parameter specifies the i18nRegion resource
          properties that the API response will include. Set the parameter
          value to snippet.

        Optional arguments:
        - hl: string
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        return self.get('i18nRegions', params=kwargs, **request_args)



    def live_broadcasts_bind(self, id_, part, request_args=None, **kwargs):
        """Bind a broadcast to a stream.

        Required arguments:
        - id_: string: Broadcast to bind to the stream
        - part: string: The *part* parameter specifies a comma-separated list
          of one or more liveBroadcast resource properties that the API
          response will include. The part names that you can include in the
          parameter value are id, snippet, contentDetails, and status.

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        - stream_id: string: Stream to bind, if not set unbind the current one.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'id_': id_, 'part': part})
        style_conv = {
            'id_': 'id',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
            'stream_id': 'streamId',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('liveBroadcasts/bind', params=kwargs, **request_args)



    def live_broadcasts_delete(self, id_, request_args=None, **kwargs):
        """Delete a given broadcast.

        Required arguments:
        - id_: string: Broadcast to delete.

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'id_': id_})
        style_conv = {
            'id_': 'id',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.delete('liveBroadcasts', params=kwargs, **request_args)



    def live_broadcasts_insert(self, part, request_args=None, **kwargs):
        """Inserts a new stream for the authenticated user.

        Required arguments:
        - part: string: The *part* parameter serves two purposes in this
          operation. It identifies the properties that the write operation
          will set as well as the properties that the API response will
          include. The part properties that you can include in the parameter
          value are id, snippet, contentDetails, and status.

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('liveBroadcasts', params=kwargs, **request_args)



    def live_broadcasts_insert_cuepoint(self, request_args=None, **kwargs):
        """Insert cuepoints in a broadcast

        Optional arguments:
        - id_: string: Broadcast to insert ads to, or equivalently
          `external_video_id` for internal use.
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        - part: string: The *part* parameter specifies a comma-separated list
          of one or more liveBroadcast resource properties that the API
          response will include. The part names that you can include in the
          parameter value are id, snippet, contentDetails, and status.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({})
        style_conv = {
            'id_': 'id',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('liveBroadcasts/cuepoint', params=kwargs, **request_args)



    def live_broadcasts_list(self, part, request_args=None, **kwargs):
        """Retrieve the list of broadcasts associated with the given channel.

        Required arguments:
        - part: string: The *part* parameter specifies a comma-separated list
          of one or more liveBroadcast resource properties that the API
          response will include. The part names that you can include in the
          parameter value are id, snippet, contentDetails, status and
          statistics.

        Optional arguments:
        - broadcast_status: string: Return broadcasts with a certain status,
          e.g. active broadcasts.
        - broadcast_type: string: Return only broadcasts with the selected type.
        - id_: string: Return broadcasts with the given ids from Stubby or
          Apiary.
        - max_results: integer: The *maxResults* parameter specifies the
          maximum number of items that should be returned in the result set.
        - mine: boolean
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        - page_token: string: The *pageToken* parameter identifies a specific
          page in the result set that should be returned. In an API response,
          the nextPageToken and prevPageToken properties identify other pages
          that could be retrieved.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'broadcast_status': 'broadcastStatus',
            'broadcast_type': 'broadcastType',
            'id_': 'id',
            'max_results': 'maxResults',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
            'page_token': 'pageToken',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('liveBroadcasts', params=kwargs, **request_args)



    def live_broadcasts_transition(self, broadcast_status, id_, part, request_args=None, **kwargs):
        """Transition a broadcast to a given status.

        Required arguments:
        - broadcast_status: string: The status to which the broadcast is going
          to transition.
        - id_: string: Broadcast to transition.
        - part: string: The *part* parameter specifies a comma-separated list
          of one or more liveBroadcast resource properties that the API
          response will include. The part names that you can include in the
          parameter value are id, snippet, contentDetails, and status.

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'broadcast_status': broadcast_status, 'id_': id_, 'part': part})
        style_conv = {
            'broadcast_status': 'broadcastStatus',
            'id_': 'id',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('liveBroadcasts/transition', params=kwargs, **request_args)



    def live_broadcasts_update(self, part, request_args=None, **kwargs):
        """Updates an existing broadcast for the authenticated user.

        Required arguments:
        - part: string: The *part* parameter serves two purposes in this
          operation. It identifies the properties that the write operation
          will set as well as the properties that the API response will
          include. The part properties that you can include in the parameter
          value are id, snippet, contentDetails, and status. Note that this
          method will override the existing values for all of the mutable
          properties that are contained in any parts that the parameter value
          specifies. For example, a broadcast's privacy status is defined in
          the status part. As such, if your request is updating a private or
          unlisted broadcast, and the request's part parameter value includes
          the status part, the broadcast's privacy setting will be updated to
          whatever value the request body specifies. If the request body does
          not specify a value, the existing privacy setting will be removed
          and the broadcast will revert to the default privacy setting.

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.put('liveBroadcasts', params=kwargs, **request_args)



    def live_chat_bans_delete(self, id_, request_args=None, **kwargs):
        """Deletes a chat ban.

        Required arguments:
        - id_: string
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'id_': id_})
        style_conv = {
            'id_': 'id',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.delete('liveChat/bans', params=kwargs, **request_args)



    def live_chat_bans_insert(self, part, request_args=None, **kwargs):
        """Inserts a new resource into this collection.

        Required arguments:
        - part: string: The *part* parameter serves two purposes in this
          operation. It identifies the properties that the write operation
          will set as well as the properties that the API response returns.
          Set the parameter value to snippet.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        return self.post('liveChat/bans', params=kwargs, **request_args)



    def live_chat_messages_delete(self, id_, request_args=None, **kwargs):
        """Deletes a chat message.

        Required arguments:
        - id_: string
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'id_': id_})
        style_conv = {
            'id_': 'id',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.delete('liveChat/messages', params=kwargs, **request_args)



    def live_chat_messages_insert(self, part, request_args=None, **kwargs):
        """Inserts a new resource into this collection.

        Required arguments:
        - part: string: The *part* parameter serves two purposes. It
          identifies the properties that the write operation will set as well
          as the properties that the API response will include. Set the
          parameter value to snippet.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        return self.post('liveChat/messages', params=kwargs, **request_args)



    def live_chat_messages_list(self, live_chat_id, part, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Required arguments:
        - live_chat_id: string: The id of the live chat for which comments
          should be returned.
        - part: string: The *part* parameter specifies the liveChatComment
          resource parts that the API response will include. Supported values
          are id, snippet, and authorDetails.

        Optional arguments:
        - hl: string: Specifies the localization language in which the system
          messages should be returned.
        - max_results: integer: The *maxResults* parameter specifies the
          maximum number of items that should be returned in the result set.
          Not used in the streaming RPC.
        - page_token: string: The *pageToken* parameter identifies a specific
          page in the result set that should be returned. In an API response,
          the nextPageToken property identify other pages that could be
          retrieved.
        - profile_image_size: integer: Specifies the size of the profile image
          that should be returned for each user.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'live_chat_id': live_chat_id, 'part': part})
        style_conv = {
            'live_chat_id': 'liveChatId',
            'max_results': 'maxResults',
            'page_token': 'pageToken',
            'profile_image_size': 'profileImageSize',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('liveChat/messages', params=kwargs, **request_args)



    def live_chat_messages_transition(self, request_args=None, **kwargs):
        """Transition a durable chat event.

        Optional arguments:
        - id_: string: The ID that uniquely identify the chat message event to
          transition.
        - status: string: The status to which the chat event is going to
          transition.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({})
        style_conv = {
            'id_': 'id',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('liveChat/messages/transition', params=kwargs, **request_args)



    def live_chat_moderators_delete(self, id_, request_args=None, **kwargs):
        """Deletes a chat moderator.

        Required arguments:
        - id_: string
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'id_': id_})
        style_conv = {
            'id_': 'id',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.delete('liveChat/moderators', params=kwargs, **request_args)



    def live_chat_moderators_insert(self, part, request_args=None, **kwargs):
        """Inserts a new resource into this collection.

        Required arguments:
        - part: string: The *part* parameter serves two purposes in this
          operation. It identifies the properties that the write operation
          will set as well as the properties that the API response returns.
          Set the parameter value to snippet.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        return self.post('liveChat/moderators', params=kwargs, **request_args)



    def live_chat_moderators_list(self, live_chat_id, part, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Required arguments:
        - live_chat_id: string: The id of the live chat for which moderators
          should be returned.
        - part: string: The *part* parameter specifies the liveChatModerator
          resource parts that the API response will include. Supported values
          are id and snippet.

        Optional arguments:
        - max_results: integer: The *maxResults* parameter specifies the
          maximum number of items that should be returned in the result set.
        - page_token: string: The *pageToken* parameter identifies a specific
          page in the result set that should be returned. In an API response,
          the nextPageToken and prevPageToken properties identify other pages
          that could be retrieved.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'live_chat_id': live_chat_id, 'part': part})
        style_conv = {
            'live_chat_id': 'liveChatId',
            'max_results': 'maxResults',
            'page_token': 'pageToken',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('liveChat/moderators', params=kwargs, **request_args)



    def live_streams_delete(self, id_, request_args=None, **kwargs):
        """Deletes an existing stream for the authenticated user.

        Required arguments:
        - id_: string

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'id_': id_})
        style_conv = {
            'id_': 'id',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.delete('liveStreams', params=kwargs, **request_args)



    def live_streams_insert(self, part, request_args=None, **kwargs):
        """Inserts a new stream for the authenticated user.

        Required arguments:
        - part: string: The *part* parameter serves two purposes in this
          operation. It identifies the properties that the write operation
          will set as well as the properties that the API response will
          include. The part properties that you can include in the parameter
          value are id, snippet, cdn, content_details, and status.

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('liveStreams', params=kwargs, **request_args)



    def live_streams_list(self, part, request_args=None, **kwargs):
        """Retrieve the list of streams associated with the given channel. --

        Required arguments:
        - part: string: The *part* parameter specifies a comma-separated list
          of one or more liveStream resource properties that the API response
          will include. The part names that you can include in the parameter
          value are id, snippet, cdn, and status.

        Optional arguments:
        - id_: string: Return LiveStreams with the given ids from Stubby or
          Apiary.
        - max_results: integer: The *maxResults* parameter specifies the
          maximum number of items that should be returned in the result set.
        - mine: boolean
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        - page_token: string: The *pageToken* parameter identifies a specific
          page in the result set that should be returned. In an API response,
          the nextPageToken and prevPageToken properties identify other pages
          that could be retrieved.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'id_': 'id',
            'max_results': 'maxResults',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
            'page_token': 'pageToken',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('liveStreams', params=kwargs, **request_args)



    def live_streams_update(self, part, request_args=None, **kwargs):
        """Updates an existing stream for the authenticated user.

        Required arguments:
        - part: string: The *part* parameter serves two purposes in this
          operation. It identifies the properties that the write operation
          will set as well as the properties that the API response will
          include. The part properties that you can include in the parameter
          value are id, snippet, cdn, and status. Note that this method will
          override the existing values for all of the mutable properties that
          are contained in any parts that the parameter value specifies. If
          the request body does not specify a value for a mutable property,
          the existing value for that property will be removed.

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.put('liveStreams', params=kwargs, **request_args)



    def members_list(self, part, request_args=None, **kwargs):
        """Retrieves a list of members that match the request criteria for a
        channel.

        Required arguments:
        - part: string: The *part* parameter specifies the member resource
          parts that the API response will include. Set the parameter value to
          snippet.

        Optional arguments:
        - filter_by_member_channel_id: string: Comma separated list of channel
          IDs. Only data about members that are part of this list will be
          included in the response.
        - has_access_to_level: string: Filter members in the results set to
          the ones that have access to a level.
        - max_results: integer: The *maxResults* parameter specifies the
          maximum number of items that should be returned in the result set.
        - mode: string: Parameter that specifies which channel members to
          return.
        - page_token: string: The *pageToken* parameter identifies a specific
          page in the result set that should be returned. In an API response,
          the nextPageToken and prevPageToken properties identify other pages
          that could be retrieved.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'filter_by_member_channel_id': 'filterByMemberChannelId',
            'has_access_to_level': 'hasAccessToLevel',
            'max_results': 'maxResults',
            'page_token': 'pageToken',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('members', params=kwargs, **request_args)



    def memberships_levels_list(self, part, request_args=None, **kwargs):
        """Retrieves a list of all pricing levels offered by a creator to the
        fans.

        Required arguments:
        - part: string: The *part* parameter specifies the membershipsLevel
          resource parts that the API response will include. Supported values
          are id and snippet.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        return self.get('membershipsLevels', params=kwargs, **request_args)



    def playlist_images_delete(self, request_args=None, **kwargs):
        """Deletes a resource.

        Optional arguments:
        - id_: string: Id to identify this image. This is returned from by the
          List method.
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({})
        style_conv = {
            'id_': 'id',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.delete('playlistImages', params=kwargs, **request_args)



    def playlist_images_insert(self, request_args=None, **kwargs):
        """Inserts a new resource into this collection.

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        - part: string: The *part* parameter specifies the properties that the
          API response will include.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({})
        style_conv = {
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('playlistImages', params=kwargs, **request_args)



    def playlist_images_list(self, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Optional arguments:
        - max_results: integer: The *maxResults* parameter specifies the
          maximum number of items that should be returned in the result set.
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        - page_token: string: The *pageToken* parameter identifies a specific
          page in the result set that should be returned. In an API response,
          the nextPageToken and prevPageToken properties identify other pages
          that could be retrieved.
        - parent: string: Return PlaylistImages for this playlist id.
        - part: string: The *part* parameter specifies a comma-separated list
          of one or more playlistImage resource properties that the API
          response will include. If the parameter identifies a property that
          contains child properties, the child properties will be included in
          the response.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({})
        style_conv = {
            'max_results': 'maxResults',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
            'page_token': 'pageToken',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('playlistImages', params=kwargs, **request_args)



    def playlist_images_update(self, request_args=None, **kwargs):
        """Updates an existing resource.

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - part: string: The *part* parameter specifies the properties that the
          API response will include.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({})
        style_conv = {
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.put('playlistImages', params=kwargs, **request_args)



    def playlist_items_delete(self, id_, request_args=None, **kwargs):
        """Deletes a resource.

        Required arguments:
        - id_: string

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'id_': id_})
        style_conv = {
            'id_': 'id',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.delete('playlistItems', params=kwargs, **request_args)



    def playlist_items_insert(self, part, request_args=None, **kwargs):
        """Inserts a new resource into this collection.

        Required arguments:
        - part: string: The *part* parameter serves two purposes in this
          operation. It identifies the properties that the write operation
          will set as well as the properties that the API response will include.

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('playlistItems', params=kwargs, **request_args)



    def playlist_items_list(self, part, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Required arguments:
        - part: string: The *part* parameter specifies a comma-separated list
          of one or more playlistItem resource properties that the API
          response will include. If the parameter identifies a property that
          contains child properties, the child properties will be included in
          the response. For example, in a playlistItem resource, the snippet
          property contains numerous fields, including the title, description,
          position, and resourceId properties. As such, if you set
          *part=snippet*, the API response will contain all of those properties.

        Optional arguments:
        - id_: string
        - max_results: integer: The *maxResults* parameter specifies the
          maximum number of items that should be returned in the result set.
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - page_token: string: The *pageToken* parameter identifies a specific
          page in the result set that should be returned. In an API response,
          the nextPageToken and prevPageToken properties identify other pages
          that could be retrieved.
        - playlist_id: string: Return the playlist items within the given
          playlist.
        - video_id: string: Return the playlist items associated with the
          given video ID.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'id_': 'id',
            'max_results': 'maxResults',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'page_token': 'pageToken',
            'playlist_id': 'playlistId',
            'video_id': 'videoId',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('playlistItems', params=kwargs, **request_args)



    def playlist_items_update(self, part, request_args=None, **kwargs):
        """Updates an existing resource.

        Required arguments:
        - part: string: The *part* parameter serves two purposes in this
          operation. It identifies the properties that the write operation
          will set as well as the properties that the API response will
          include. Note that this method will override the existing values for
          all of the mutable properties that are contained in any parts that
          the parameter value specifies. For example, a playlist item can
          specify a start time and end time, which identify the times portion
          of the video that should play when users watch the video in the
          playlist. If your request is updating a playlist item that sets
          these values, and the request's part parameter value includes the
          contentDetails part, the playlist item's start and end times will be
          updated to whatever value the request body specifies. If the request
          body does not specify values, the existing start and end times will
          be removed and replaced with the default settings.

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.put('playlistItems', params=kwargs, **request_args)



    def playlists_delete(self, id_, request_args=None, **kwargs):
        """Deletes a resource.

        Required arguments:
        - id_: string

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'id_': id_})
        style_conv = {
            'id_': 'id',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.delete('playlists', params=kwargs, **request_args)



    def playlists_insert(self, part, request_args=None, **kwargs):
        """Inserts a new resource into this collection.

        Required arguments:
        - part: string: The *part* parameter serves two purposes in this
          operation. It identifies the properties that the write operation
          will set as well as the properties that the API response will include.

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('playlists', params=kwargs, **request_args)



    def playlists_list(self, part, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Required arguments:
        - part: string: The *part* parameter specifies a comma-separated list
          of one or more playlist resource properties that the API response
          will include. If the parameter identifies a property that contains
          child properties, the child properties will be included in the
          response. For example, in a playlist resource, the snippet property
          contains properties like author, title, description, tags, and
          timeCreated. As such, if you set *part=snippet*, the API response
          will contain all of those properties.

        Optional arguments:
        - channel_id: string: Return the playlists owned by the specified
          channel ID.
        - hl: string: Return content in specified language
        - id_: string: Return the playlists with the given IDs for Stubby or
          Apiary.
        - max_results: integer: The *maxResults* parameter specifies the
          maximum number of items that should be returned in the result set.
        - mine: boolean: Return the playlists owned by the authenticated user.
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        - page_token: string: The *pageToken* parameter identifies a specific
          page in the result set that should be returned. In an API response,
          the nextPageToken and prevPageToken properties identify other pages
          that could be retrieved.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'channel_id': 'channelId',
            'id_': 'id',
            'max_results': 'maxResults',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
            'page_token': 'pageToken',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('playlists', params=kwargs, **request_args)



    def playlists_update(self, part, request_args=None, **kwargs):
        """Updates an existing resource.

        Required arguments:
        - part: string: The *part* parameter serves two purposes in this
          operation. It identifies the properties that the write operation
          will set as well as the properties that the API response will
          include. Note that this method will override the existing values for
          mutable properties that are contained in any parts that the request
          body specifies. For example, a playlist's description is contained
          in the snippet part, which must be included in the request body. If
          the request does not specify a value for the snippet.description
          property, the playlist's existing description will be deleted.

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.put('playlists', params=kwargs, **request_args)



    def search_list(self, part, request_args=None, **kwargs):
        """Retrieves a list of search resources

        Required arguments:
        - part: string: The *part* parameter specifies a comma-separated list
          of one or more search resource properties that the API response will
          include. Set the parameter value to snippet.

        Optional arguments:
        - channel_id: string: Filter on resources belonging to this channelId.
        - channel_type: string: Add a filter on the channel search.
        - event_type: string: Filter on the livestream status of the videos.
        - for_content_owner: boolean: Search owned by a content owner.
        - for_developer: boolean: Restrict the search to only retrieve videos
          uploaded using the project id of the authenticated user.
        - for_mine: boolean: Search for the private videos of the
          authenticated user.
        - location: string: Filter on location of the video
        - location_radius: string: Filter on distance from the location
          (specified above).
        - max_results: integer: The *maxResults* parameter specifies the
          maximum number of items that should be returned in the result set.
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - order: string: Sort order of the results.
        - page_token: string: The *pageToken* parameter identifies a specific
          page in the result set that should be returned. In an API response,
          the nextPageToken and prevPageToken properties identify other pages
          that could be retrieved.
        - published_after: string: Filter on resources published after this
          date.
        - published_before: string: Filter on resources published before this
          date.
        - q: string: Textual search terms to match.
        - region_code: string: Display the content as seen by viewers in this
          country.
        - relevance_language: string: Return results relevant to this language.
        - safe_search: string: Indicates whether the search results should
          include restricted content as well as standard content.
        - topic_id: string: Restrict results to a particular topic.
        - type_: string: Restrict results to a particular set of resource
          types from One Platform.
        - video_caption: string: Filter on the presence of captions on the
          videos.
        - video_category_id: string: Filter on videos in a specific category.
        - video_definition: string: Filter on the definition of the videos.
        - video_dimension: string: Filter on 3d videos.
        - video_duration: string: Filter on the duration of the videos.
        - video_embeddable: string: Filter on embeddable videos.
        - video_license: string: Filter on the license of the videos.
        - video_paid_product_placement: string
        - video_syndicated: string: Filter on syndicated videos.
        - video_type: string: Filter on videos of a specific type.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'channel_id': 'channelId',
            'channel_type': 'channelType',
            'event_type': 'eventType',
            'for_content_owner': 'forContentOwner',
            'for_developer': 'forDeveloper',
            'for_mine': 'forMine',
            'location_radius': 'locationRadius',
            'max_results': 'maxResults',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'page_token': 'pageToken',
            'published_after': 'publishedAfter',
            'published_before': 'publishedBefore',
            'region_code': 'regionCode',
            'relevance_language': 'relevanceLanguage',
            'safe_search': 'safeSearch',
            'topic_id': 'topicId',
            'type_': 'type',
            'video_caption': 'videoCaption',
            'video_category_id': 'videoCategoryId',
            'video_definition': 'videoDefinition',
            'video_dimension': 'videoDimension',
            'video_duration': 'videoDuration',
            'video_embeddable': 'videoEmbeddable',
            'video_license': 'videoLicense',
            'video_paid_product_placement': 'videoPaidProductPlacement',
            'video_syndicated': 'videoSyndicated',
            'video_type': 'videoType',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('search', params=kwargs, **request_args)



    def subscriptions_delete(self, id_, request_args=None, **kwargs):
        """Deletes a resource.

        Required arguments:
        - id_: string
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'id_': id_})
        style_conv = {
            'id_': 'id',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.delete('subscriptions', params=kwargs, **request_args)



    def subscriptions_insert(self, part, request_args=None, **kwargs):
        """Inserts a new resource into this collection.

        Required arguments:
        - part: string: The *part* parameter serves two purposes in this
          operation. It identifies the properties that the write operation
          will set as well as the properties that the API response will include.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        return self.post('subscriptions', params=kwargs, **request_args)



    def subscriptions_list(self, part, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Required arguments:
        - part: string: The *part* parameter specifies a comma-separated list
          of one or more subscription resource properties that the API
          response will include. If the parameter identifies a property that
          contains child properties, the child properties will be included in
          the response. For example, in a subscription resource, the snippet
          property contains other properties, such as a display title for the
          subscription. If you set *part=snippet*, the API response will also
          contain all of those nested properties.

        Optional arguments:
        - channel_id: string: Return the subscriptions of the given channel
          owner.
        - for_channel_id: string: Return the subscriptions to the subset of
          these channels that the authenticated user is subscribed to.
        - id_: string: Return the subscriptions with the given IDs for Stubby
          or Apiary.
        - max_results: integer: The *maxResults* parameter specifies the
          maximum number of items that should be returned in the result set.
        - mine: boolean: Flag for returning the subscriptions of the
          authenticated user.
        - my_recent_subscribers: boolean
        - my_subscribers: boolean: Return the subscribers of the given channel
          owner.
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        - order: string: The order of the returned subscriptions
        - page_token: string: The *pageToken* parameter identifies a specific
          page in the result set that should be returned. In an API response,
          the nextPageToken and prevPageToken properties identify other pages
          that could be retrieved.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'channel_id': 'channelId',
            'for_channel_id': 'forChannelId',
            'id_': 'id',
            'max_results': 'maxResults',
            'my_recent_subscribers': 'myRecentSubscribers',
            'my_subscribers': 'mySubscribers',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
            'page_token': 'pageToken',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('subscriptions', params=kwargs, **request_args)



    def super_chat_events_list(self, part, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Required arguments:
        - part: string: The *part* parameter specifies the superChatEvent
          resource parts that the API response will include. This parameter is
          currently not supported.

        Optional arguments:
        - hl: string: Return rendered funding amounts in specified language.
        - max_results: integer: The *maxResults* parameter specifies the
          maximum number of items that should be returned in the result set.
        - page_token: string: The *pageToken* parameter identifies a specific
          page in the result set that should be returned. In an API response,
          the nextPageToken and prevPageToken properties identify other pages
          that could be retrieved.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'max_results': 'maxResults',
            'page_token': 'pageToken',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('superChatEvents', params=kwargs, **request_args)



    def tests_insert(self, part, request_args=None, **kwargs):
        """POST method.

        Required arguments:
        - part: string

        Optional arguments:
        - external_channel_id: string
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'external_channel_id': 'externalChannelId',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('tests', params=kwargs, **request_args)



    def third_party_links_delete(self, linking_token, type_, request_args=None, **kwargs):
        """Deletes a resource.

        Required arguments:
        - linking_token: string: Delete the partner links with the given
          linking token.
        - type_: string: Type of the link to be deleted.

        Optional arguments:
        - external_channel_id: string: Channel ID to which changes should be
          applied, for delegation.
        - part: string: Do not use. Required for compatibility.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'linking_token': linking_token, 'type_': type_})
        style_conv = {
            'external_channel_id': 'externalChannelId',
            'linking_token': 'linkingToken',
            'type_': 'type',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.delete('thirdPartyLinks', params=kwargs, **request_args)



    def third_party_links_insert(self, part, request_args=None, **kwargs):
        """Inserts a new resource into this collection.

        Required arguments:
        - part: string: The *part* parameter specifies the thirdPartyLink
          resource parts that the API request and response will include.
          Supported values are linkingToken, status, and snippet.

        Optional arguments:
        - external_channel_id: string: Channel ID to which changes should be
          applied, for delegation.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'external_channel_id': 'externalChannelId',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('thirdPartyLinks', params=kwargs, **request_args)



    def third_party_links_list(self, part, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Required arguments:
        - part: string: The *part* parameter specifies the thirdPartyLink
          resource parts that the API response will include. Supported values
          are linkingToken, status, and snippet.

        Optional arguments:
        - external_channel_id: string: Channel ID to which changes should be
          applied, for delegation.
        - linking_token: string: Get a third party link with the given linking
          token.
        - type_: string: Get a third party link of the given type.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'external_channel_id': 'externalChannelId',
            'linking_token': 'linkingToken',
            'type_': 'type',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('thirdPartyLinks', params=kwargs, **request_args)



    def third_party_links_update(self, part, request_args=None, **kwargs):
        """Updates an existing resource.

        Required arguments:
        - part: string: The *part* parameter specifies the thirdPartyLink
          resource parts that the API request and response will include.
          Supported values are linkingToken, status, and snippet.

        Optional arguments:
        - external_channel_id: string: Channel ID to which changes should be
          applied, for delegation.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'external_channel_id': 'externalChannelId',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.put('thirdPartyLinks', params=kwargs, **request_args)



    def thumbnails_set(self, video_id, request_args=None, **kwargs):
        """As this is not an insert in a strict sense (it supports
        uploading/setting of a thumbnail for multiple videos, which doesn't
        result in creation of a single resource), I use a custom verb here.

        Required arguments:
        - video_id: string: Returns the Thumbnail with the given video IDs for
          Stubby or Apiary.

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The actual CMS account that the user
          authenticates with must be linked to the specified YouTube content
          owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'video_id': video_id})
        style_conv = {
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'video_id': 'videoId',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('thumbnails/set', params=kwargs, **request_args)



    def video_abuse_report_reasons_list(self, part, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Required arguments:
        - part: string: The *part* parameter specifies the videoCategory
          resource parts that the API response will include. Supported values
          are id and snippet.

        Optional arguments:
        - hl: string
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        return self.get('videoAbuseReportReasons', params=kwargs, **request_args)



    def video_categories_list(self, part, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Required arguments:
        - part: string: The *part* parameter specifies the videoCategory
          resource properties that the API response will include. Set the
          parameter value to snippet.

        Optional arguments:
        - hl: string
        - id_: string: Returns the video categories with the given IDs for
          Stubby or Apiary.
        - region_code: string
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'id_': 'id',
            'region_code': 'regionCode',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('videoCategories', params=kwargs, **request_args)



    def video_trainability_get(self, request_args=None, **kwargs):
        """Returns the trainability status of a video.

        Optional arguments:
        - id_: string: The ID of the video to retrieve.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({})
        style_conv = {
            'id_': 'id',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('videoTrainability', params=kwargs, **request_args)



    def videos_delete(self, id_, request_args=None, **kwargs):
        """Deletes a resource.

        Required arguments:
        - id_: string

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The actual CMS account that the user
          authenticates with must be linked to the specified YouTube content
          owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'id_': id_})
        style_conv = {
            'id_': 'id',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.delete('videos', params=kwargs, **request_args)



    def videos_get_rating(self, id_, request_args=None, **kwargs):
        """Retrieves the ratings that the authorized user gave to a list of
        specified videos.

        Required arguments:
        - id_: string

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'id_': id_})
        style_conv = {
            'id_': 'id',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('videos/getRating', params=kwargs, **request_args)



    def videos_insert(self, part, request_args=None, **kwargs):
        """Inserts a new resource into this collection.

        Required arguments:
        - part: string: The *part* parameter serves two purposes in this
          operation. It identifies the properties that the write operation
          will set as well as the properties that the API response will
          include. Note that not all parts contain properties that can be set
          when inserting or updating a video. For example, the statistics
          object encapsulates statistics that YouTube calculates for a video
          and does not contain values that you can set or modify. If the
          parameter value specifies a part that does not contain mutable
          values, that part will still be included in the API response.

        Optional arguments:
        - auto_levels: boolean: Should auto-levels be applied to the upload.
        - notify_subscribers: boolean: Notify the channel subscribers about
          the new video. As default, the notification is enabled.
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - on_behalf_of_content_owner_channel: string: This parameter can only
          be used in a properly authorized request. *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwnerChannel* parameter specifies the YouTube
          channel ID of the channel to which a video is being added. This
          parameter is required when a request specifies a value for the
          onBehalfOfContentOwner parameter, and it can only be used in
          conjunction with that parameter. In addition, the request must be
          authorized using a CMS account that is linked to the content owner
          that the onBehalfOfContentOwner parameter specifies. Finally, the
          channel that the onBehalfOfContentOwnerChannel parameter value
          specifies must be linked to the content owner that the
          onBehalfOfContentOwner parameter specifies. This parameter is
          intended for YouTube content partners that own and manage many
          different YouTube channels. It allows content owners to authenticate
          once and perform actions on behalf of the channel specified in the
          parameter value, without having to provide authentication
          credentials for each separate channel.
        - stabilize: boolean: Should stabilize be applied to the upload.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'auto_levels': 'autoLevels',
            'notify_subscribers': 'notifySubscribers',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'on_behalf_of_content_owner_channel': 'onBehalfOfContentOwnerChannel',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('videos', params=kwargs, **request_args)



    def videos_list(self, part, request_args=None, **kwargs):
        """Retrieves a list of resources, possibly filtered.

        Required arguments:
        - part: string: The *part* parameter specifies a comma-separated list
          of one or more video resource properties that the API response will
          include. If the parameter identifies a property that contains child
          properties, the child properties will be included in the response.
          For example, in a video resource, the snippet property contains the
          channelId, title, description, tags, and categoryId properties. As
          such, if you set *part=snippet*, the API response will contain all
          of those properties.

        Optional arguments:
        - chart: string: Return the videos that are in the specified chart.
        - hl: string: Stands for "host language". Specifies the localization
          language of the metadata to be filled into snippet.localized. The
          field is filled with the default metadata if there is no
          localization in the specified language. The parameter value must be
          a language code included in the list returned by the
          i18nLanguages.list method (e.g. en_US, es_MX).
        - id_: string: Return videos with the given ids.
        - locale: string
        - max_height: integer
        - max_results: integer: The *maxResults* parameter specifies the
          maximum number of items that should be returned in the result set.
          *Note:* This parameter is supported for use in conjunction with the
          myRating and chart parameters, but it is not supported for use in
          conjunction with the id parameter.
        - max_width: integer: Return the player with maximum height specified in
        - my_rating: string: Return videos liked/disliked by the authenticated
          user. Does not support RateType.RATED_TYPE_NONE.
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        - page_token: string: The *pageToken* parameter identifies a specific
          page in the result set that should be returned. In an API response,
          the nextPageToken and prevPageToken properties identify other pages
          that could be retrieved. *Note:* This parameter is supported for use
          in conjunction with the myRating and chart parameters, but it is not
          supported for use in conjunction with the id parameter.
        - region_code: string: Use a chart that is specific to the specified
          region
        - video_category_id: string: Use chart that is specific to the
          specified video category
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'id_': 'id',
            'max_height': 'maxHeight',
            'max_results': 'maxResults',
            'max_width': 'maxWidth',
            'my_rating': 'myRating',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
            'page_token': 'pageToken',
            'region_code': 'regionCode',
            'video_category_id': 'videoCategoryId',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.get('videos', params=kwargs, **request_args)



    def videos_rate(self, id_, rating, request_args=None, **kwargs):
        """Adds a like or dislike rating to a video or removes a rating from a
        video.

        Required arguments:
        - id_: string
        - rating: string
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'id_': id_, 'rating': rating})
        style_conv = {
            'id_': 'id',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('videos/rate', params=kwargs, **request_args)



    def videos_report_abuse(self, request_args=None, **kwargs):
        """Report abuse for a video.

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({})
        style_conv = {
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('videos/reportAbuse', params=kwargs, **request_args)



    def videos_update(self, part, request_args=None, **kwargs):
        """Updates an existing resource.

        Required arguments:
        - part: string: The *part* parameter serves two purposes in this
          operation. It identifies the properties that the write operation
          will set as well as the properties that the API response will
          include. Note that this method will override the existing values for
          all of the mutable properties that are contained in any parts that
          the parameter value specifies. For example, a video's privacy
          setting is contained in the status part. As such, if your request is
          updating a private video, and the request's part parameter value
          includes the status part, the video's privacy setting will be
          updated to whatever value the request body specifies. If the request
          body does not specify a value, the existing privacy setting will be
          removed and the video will revert to the default privacy setting. In
          addition, not all parts contain properties that can be set when
          inserting or updating a video. For example, the statistics object
          encapsulates statistics that YouTube calculates for a video and does
          not contain values that you can set or modify. If the parameter
          value specifies a part that does not contain mutable values, that
          part will still be included in the API response.

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The actual CMS account that the user
          authenticates with must be linked to the specified YouTube content
          owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'part': part})
        style_conv = {
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.put('videos', params=kwargs, **request_args)



    def watermarks_set(self, channel_id, request_args=None, **kwargs):
        """Allows upload of watermark image and setting it for a channel.

        Required arguments:
        - channel_id: string

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'channel_id': channel_id})
        style_conv = {
            'channel_id': 'channelId',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('watermarks/set', params=kwargs, **request_args)



    def watermarks_unset(self, channel_id, request_args=None, **kwargs):
        """Allows removal of channel watermark.

        Required arguments:
        - channel_id: string

        Optional arguments:
        - on_behalf_of_content_owner: string: *Note:* This parameter is
          intended exclusively for YouTube content partners. The
          *onBehalfOfContentOwner* parameter indicates that the request's
          authorization credentials identify a YouTube CMS user who is acting
          on behalf of the content owner specified in the parameter value.
          This parameter is intended for YouTube content partners that own and
          manage many different YouTube channels. It allows content owners to
          authenticate once and get access to all their video and channel
          data, without having to provide authentication credentials for each
          individual channel. The CMS account that the user authenticates with
          must be linked to the specified YouTube content owner.
        """

        if request_args is None:
            request_args = {}
        kwargs.update({'channel_id': channel_id})
        style_conv = {
            'channel_id': 'channelId',
            'on_behalf_of_content_owner': 'onBehalfOfContentOwner',
        }
        kwargs = {style_conv.get(k, k): v for k, v in kwargs.items()}
        return self.post('watermarks/unset', params=kwargs, **request_args)



    api_help = {
        'abuse_reports_insert': {
            'help': 'Inserts a new resource into this collection.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter serves two purposes in this '
                            'operation. It identifies the properties that the '
                            'write operation will set as well as the '
                            'properties that the API response will include.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [],
            'method': abuse_reports_insert,
            'FQMN': ['youtube', 'abuse_reports', 'insert'],
        },
        'activities_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies a comma-separated '
                            'list of one or more activity resource properties '
                            'that the API response will include. If the '
                            'parameter identifies a property that contains '
                            'child properties, the child properties will be '
                            'included in the response. For example, in an '
                            'activity resource, the snippet property contains '
                            'other properties that identify the type of '
                            'activity, a display title for the activity, and '
                            'so forth. If you set *part=snippet*, the API '
                            'response will also contain all of those nested '
                            'properties.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'channelId',
                    'name': 'channel_id',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'home',
                    'name': 'home',
                    'type': 'boolean',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'maxResults',
                    'name': 'max_results',
                    'type': 'integer',
                    'help': 'The *maxResults* parameter specifies the maximum '
                            'number of items that should be returned in the '
                            'result set.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'mine',
                    'name': 'mine',
                    'type': 'boolean',
                    'help': None,
                    'deprecated': True,
                    'repeated': False,
                },
                {
                    'originalName': 'pageToken',
                    'name': 'page_token',
                    'type': 'string',
                    'help': 'The *pageToken* parameter identifies a specific '
                            'page in the result set that should be returned. '
                            'In an API response, the nextPageToken and '
                            'prevPageToken properties identify other pages '
                            'that could be retrieved.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'publishedAfter',
                    'name': 'published_after',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'publishedBefore',
                    'name': 'published_before',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'regionCode',
                    'name': 'region_code',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': activities_list,
            'FQMN': ['youtube', 'activities', 'list'],
        },
        'captions_delete': {
            'help': 'Deletes a resource.',
            'required_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOf',
                    'name': 'on_behalf_of',
                    'type': 'string',
                    'help': 'ID of the Google+ Page for the channel that the '
                            'request is be on behalf of',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The '
                            'actual CMS account that the user authenticates '
                            'with must be linked to the specified YouTube '
                            'content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': captions_delete,
            'FQMN': ['youtube', 'captions', 'delete'],
        },
        'captions_download': {
            'help': 'Downloads a caption track.',
            'required_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'The ID of the caption track to download, '
                            'required for One Platform.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOf',
                    'name': 'on_behalf_of',
                    'type': 'string',
                    'help': 'ID of the Google+ Page for the channel that the '
                            'request is be on behalf of',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The '
                            'actual CMS account that the user authenticates '
                            'with must be linked to the specified YouTube '
                            'content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'tfmt',
                    'name': 'tfmt',
                    'type': 'string',
                    'help': 'Convert the captions into this format. Supported '
                            'options are sbv, srt, and vtt.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'tlang',
                    'name': 'tlang',
                    'type': 'string',
                    'help': 'tlang is the language code; machine translate '
                            'the captions into this language.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': captions_download,
            'FQMN': ['youtube', 'captions', 'download'],
        },
        'captions_insert': {
            'help': 'Inserts a new resource into this collection.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies the caption '
                            'resource parts that the API response will '
                            'include. Set the parameter value to snippet.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOf',
                    'name': 'on_behalf_of',
                    'type': 'string',
                    'help': 'ID of the Google+ Page for the channel that the '
                            'request is be on behalf of',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The '
                            'actual CMS account that the user authenticates '
                            'with must be linked to the specified YouTube '
                            'content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'sync',
                    'name': 'sync',
                    'type': 'boolean',
                    'help': 'Extra parameter to allow automatically syncing '
                            'the uploaded caption/transcript with the audio.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': captions_insert,
            'FQMN': ['youtube', 'captions', 'insert'],
        },
        'captions_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies a comma-separated '
                            'list of one or more caption resource parts that '
                            'the API response will include. The part names '
                            'that you can include in the parameter value are '
                            'id and snippet.',
                    'deprecated': False,
                    'repeated': True,
                },
                {
                    'originalName': 'videoId',
                    'name': 'video_id',
                    'type': 'string',
                    'help': 'Returns the captions for the specified video.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'Returns the captions with the given IDs for '
                            'Stubby or Apiary.',
                    'deprecated': False,
                    'repeated': True,
                },
                {
                    'originalName': 'onBehalfOf',
                    'name': 'on_behalf_of',
                    'type': 'string',
                    'help': 'ID of the Google+ Page for the channel that the '
                            'request is on behalf of.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The '
                            'actual CMS account that the user authenticates '
                            'with must be linked to the specified YouTube '
                            'content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': captions_list,
            'FQMN': ['youtube', 'captions', 'list'],
        },
        'captions_update': {
            'help': 'Updates an existing resource.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies a comma-separated '
                            'list of one or more caption resource parts that '
                            'the API response will include. The part names '
                            'that you can include in the parameter value are '
                            'id and snippet.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOf',
                    'name': 'on_behalf_of',
                    'type': 'string',
                    'help': 'ID of the Google+ Page for the channel that the '
                            'request is on behalf of.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The '
                            'actual CMS account that the user authenticates '
                            'with must be linked to the specified YouTube '
                            'content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'sync',
                    'name': 'sync',
                    'type': 'boolean',
                    'help': 'Extra parameter to allow automatically syncing '
                            'the uploaded caption/transcript with the audio.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': captions_update,
            'FQMN': ['youtube', 'captions', 'update'],
        },
        'channel_banners_insert': {
            'help': 'Inserts a new resource into this collection.',
            'required_params': [],
            'optional_params': [
                {
                    'originalName': 'channelId',
                    'name': 'channel_id',
                    'type': 'string',
                    'help': 'Unused, channel_id is currently derived from the '
                            'security context of the requestor.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The '
                            'actual CMS account that the user authenticates '
                            'with must be linked to the specified YouTube '
                            'content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': channel_banners_insert,
            'FQMN': ['youtube', 'channel_banners', 'insert'],
        },
        'channel_sections_delete': {
            'help': 'Deletes a resource.',
            'required_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': channel_sections_delete,
            'FQMN': ['youtube', 'channel_sections', 'delete'],
        },
        'channel_sections_insert': {
            'help': 'Inserts a new resource into this collection.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter serves two purposes in this '
                            'operation. It identifies the properties that the '
                            'write operation will set as well as the '
                            'properties that the API response will include. '
                            'The part names that you can include in the '
                            'parameter value are snippet and contentDetails.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': channel_sections_insert,
            'FQMN': ['youtube', 'channel_sections', 'insert'],
        },
        'channel_sections_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies a comma-separated '
                            'list of one or more channelSection resource '
                            'properties that the API response will include. '
                            'The part names that you can include in the '
                            'parameter value are id, snippet, and '
                            'contentDetails. If the parameter identifies a '
                            'property that contains child properties, the '
                            'child properties will be included in the '
                            'response. For example, in a channelSection '
                            'resource, the snippet property contains other '
                            'properties, such as a display title for the '
                            'channelSection. If you set *part=snippet*, the '
                            'API response will also contain all of those '
                            'nested properties.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'channelId',
                    'name': 'channel_id',
                    'type': 'string',
                    'help': 'Return the ChannelSections owned by the '
                            'specified channel ID.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'hl',
                    'name': 'hl',
                    'type': 'string',
                    'help': 'Return content in specified language',
                    'deprecated': True,
                    'repeated': False,
                },
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'Return the ChannelSections with the given IDs '
                            'for Stubby or Apiary.',
                    'deprecated': False,
                    'repeated': True,
                },
                {
                    'originalName': 'mine',
                    'name': 'mine',
                    'type': 'boolean',
                    'help': 'Return the ChannelSections owned by the '
                            'authenticated user.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': channel_sections_list,
            'FQMN': ['youtube', 'channel_sections', 'list'],
        },
        'channel_sections_update': {
            'help': 'Updates an existing resource.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter serves two purposes in this '
                            'operation. It identifies the properties that the '
                            'write operation will set as well as the '
                            'properties that the API response will include. '
                            'The part names that you can include in the '
                            'parameter value are snippet and contentDetails.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': channel_sections_update,
            'FQMN': ['youtube', 'channel_sections', 'update'],
        },
        'channels_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies a comma-separated '
                            'list of one or more channel resource properties '
                            'that the API response will include. If the '
                            'parameter identifies a property that contains '
                            'child properties, the child properties will be '
                            'included in the response. For example, in a '
                            'channel resource, the contentDetails property '
                            'contains other properties, such as the uploads '
                            'properties. As such, if you set '
                            '*part=contentDetails*, the API response will '
                            'also contain all of those nested properties.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'categoryId',
                    'name': 'category_id',
                    'type': 'string',
                    'help': 'Return the channels within the specified guide '
                            'category ID.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'forHandle',
                    'name': 'for_handle',
                    'type': 'string',
                    'help': 'Return the channel associated with a YouTube '
                            'handle.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'forUsername',
                    'name': 'for_username',
                    'type': 'string',
                    'help': 'Return the channel associated with a YouTube '
                            'username.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'hl',
                    'name': 'hl',
                    'type': 'string',
                    'help': 'Stands for "host language". Specifies the '
                            'localization language of the metadata to be '
                            'filled into snippet.localized. The field is '
                            'filled with the default metadata if there is no '
                            'localization in the specified language. The '
                            'parameter value must be a language code included '
                            'in the list returned by the i18nLanguages.list '
                            'method (e.g. en_US, es_MX).',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'Return the channels with the specified IDs.',
                    'deprecated': False,
                    'repeated': True,
                },
                {
                    'originalName': 'managedByMe',
                    'name': 'managed_by_me',
                    'type': 'boolean',
                    'help': 'Return the channels managed by the authenticated '
                            'user.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'maxResults',
                    'name': 'max_results',
                    'type': 'integer',
                    'help': 'The *maxResults* parameter specifies the maximum '
                            'number of items that should be returned in the '
                            'result set.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'mine',
                    'name': 'mine',
                    'type': 'boolean',
                    'help': 'Return the ids of channels owned by the '
                            'authenticated user.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'mySubscribers',
                    'name': 'my_subscribers',
                    'type': 'boolean',
                    'help': 'Return the channels subscribed to the '
                            'authenticated user',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'pageToken',
                    'name': 'page_token',
                    'type': 'string',
                    'help': 'The *pageToken* parameter identifies a specific '
                            'page in the result set that should be returned. '
                            'In an API response, the nextPageToken and '
                            'prevPageToken properties identify other pages '
                            'that could be retrieved.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': channels_list,
            'FQMN': ['youtube', 'channels', 'list'],
        },
        'channels_update': {
            'help': 'Updates an existing resource.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter serves two purposes in this '
                            'operation. It identifies the properties that the '
                            'write operation will set as well as the '
                            'properties that the API response will include. '
                            'The API currently only allows the parameter '
                            'value to be set to either brandingSettings or '
                            'invideoPromotion. (You cannot update both of '
                            'those parts with a single request.) Note that '
                            'this method overrides the existing values for '
                            'all of the mutable properties that are contained '
                            'in any parts that the parameter value specifies.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': 'The *onBehalfOfContentOwner* parameter indicates '
                            'that the authenticated user is acting on behalf '
                            'of the content owner specified in the parameter '
                            'value. This parameter is intended for YouTube '
                            'content partners that own and manage many '
                            'different YouTube channels. It allows content '
                            'owners to authenticate once and get access to '
                            'all their video and channel data, without having '
                            'to provide authentication credentials for each '
                            'individual channel. The actual CMS account that '
                            'the user authenticates with needs to be linked '
                            'to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': channels_update,
            'FQMN': ['youtube', 'channels', 'update'],
        },
        'comment_threads_insert': {
            'help': 'Inserts a new resource into this collection.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter identifies the properties '
                            'that the API response will include. Set the '
                            'parameter value to snippet. The snippet part has '
                            'a quota cost of 2 units.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [],
            'method': comment_threads_insert,
            'FQMN': ['youtube', 'comment_threads', 'insert'],
        },
        'comment_threads_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies a comma-separated '
                            'list of one or more commentThread resource '
                            'properties that the API response will include.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'allThreadsRelatedToChannelId',
                    'name': 'all_threads_related_to_channel_id',
                    'type': 'string',
                    'help': 'Returns the comment threads of all videos of the '
                            'channel and the channel comments as well.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'channelId',
                    'name': 'channel_id',
                    'type': 'string',
                    'help': 'Returns the comment threads for all the channel '
                            'comments (ie does not include comments left on '
                            'videos).',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'Returns the comment threads with the given IDs '
                            'for Stubby or Apiary.',
                    'deprecated': False,
                    'repeated': True,
                },
                {
                    'originalName': 'maxResults',
                    'name': 'max_results',
                    'type': 'integer',
                    'help': 'The *maxResults* parameter specifies the maximum '
                            'number of items that should be returned in the '
                            'result set.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'moderationStatus',
                    'name': 'moderation_status',
                    'type': 'string',
                    'help': 'Limits the returned comment threads to those '
                            'with the specified moderation status. Not '
                            "compatible with the 'id' filter. Valid values: "
                            'published, heldForReview, likelySpam.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'order',
                    'name': 'order',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'pageToken',
                    'name': 'page_token',
                    'type': 'string',
                    'help': 'The *pageToken* parameter identifies a specific '
                            'page in the result set that should be returned. '
                            'In an API response, the nextPageToken and '
                            'prevPageToken properties identify other pages '
                            'that could be retrieved.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'postId',
                    'name': 'post_id',
                    'type': 'string',
                    'help': 'Returns the comment threads of the specified post.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'searchTerms',
                    'name': 'search_terms',
                    'type': 'string',
                    'help': 'Limits the returned comment threads to those '
                            'matching the specified key words. Not compatible '
                            "with the 'id' filter.",
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'textFormat',
                    'name': 'text_format',
                    'type': 'string',
                    'help': 'The requested text format for the returned '
                            'comments.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'videoId',
                    'name': 'video_id',
                    'type': 'string',
                    'help': 'Returns the comment threads of the specified '
                            'video.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': comment_threads_list,
            'FQMN': ['youtube', 'comment_threads', 'list'],
        },
        'comments_delete': {
            'help': 'Deletes a resource.',
            'required_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [],
            'method': comments_delete,
            'FQMN': ['youtube', 'comments', 'delete'],
        },
        'comments_insert': {
            'help': 'Inserts a new resource into this collection.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter identifies the properties '
                            'that the API response will include. Set the '
                            'parameter value to snippet. The snippet part has '
                            'a quota cost of 2 units.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [],
            'method': comments_insert,
            'FQMN': ['youtube', 'comments', 'insert'],
        },
        'comments_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies a comma-separated '
                            'list of one or more comment resource properties '
                            'that the API response will include.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'Returns the comments with the given IDs for One '
                            'Platform.',
                    'deprecated': False,
                    'repeated': True,
                },
                {
                    'originalName': 'maxResults',
                    'name': 'max_results',
                    'type': 'integer',
                    'help': 'The *maxResults* parameter specifies the maximum '
                            'number of items that should be returned in the '
                            'result set.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'pageToken',
                    'name': 'page_token',
                    'type': 'string',
                    'help': 'The *pageToken* parameter identifies a specific '
                            'page in the result set that should be returned. '
                            'In an API response, the nextPageToken and '
                            'prevPageToken properties identify other pages '
                            'that could be retrieved.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'parentId',
                    'name': 'parent_id',
                    'type': 'string',
                    'help': 'Returns replies to the specified comment. Note, '
                            'currently YouTube features only one level of '
                            'replies (ie replies to top level comments). '
                            'However replies to replies may be supported in '
                            'the future.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'textFormat',
                    'name': 'text_format',
                    'type': 'string',
                    'help': 'The requested text format for the returned '
                            'comments.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': comments_list,
            'FQMN': ['youtube', 'comments', 'list'],
        },
        'comments_mark_as_spam': {
            'help': "Expresses the caller's opinion that one or more comments "
            'should be flagged as spam.',
            'required_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'Flags the comments with the given IDs as spam in '
                            "the caller's opinion.",
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [],
            'method': comments_mark_as_spam,
            'FQMN': ['youtube', 'comments', 'mark_as_spam'],
        },
        'comments_set_moderation_status': {
            'help': 'Sets the moderation status of one or more comments.',
            'required_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'Modifies the moderation status of the comments '
                            'with the given IDs',
                    'deprecated': False,
                    'repeated': True,
                },
                {
                    'originalName': 'moderationStatus',
                    'name': 'moderation_status',
                    'type': 'string',
                    'help': 'Specifies the requested moderation status. Note, '
                            'comments can be in statuses, which are not '
                            'available through this call. For example, this '
                            "call does not allow to mark a comment as 'likely "
                            "spam'. Valid values: 'heldForReview', "
                            "'published' or 'rejected'.",
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'banAuthor',
                    'name': 'ban_author',
                    'type': 'boolean',
                    'help': 'If set to true the author of the comment gets '
                            'added to the ban list. This means all future '
                            'comments of the author will autmomatically be '
                            'rejected. Only valid in combination with '
                            'STATUS_REJECTED.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': comments_set_moderation_status,
            'FQMN': ['youtube', 'comments', 'set_moderation_status'],
        },
        'comments_update': {
            'help': 'Updates an existing resource.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter identifies the properties '
                            'that the API response will include. You must at '
                            'least include the snippet part in the parameter '
                            'value since that part contains all of the '
                            'properties that the API request can update.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [],
            'method': comments_update,
            'FQMN': ['youtube', 'comments', 'update'],
        },
        'i18n_languages_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies the i18nLanguage '
                            'resource properties that the API response will '
                            'include. Set the parameter value to snippet.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'hl',
                    'name': 'hl',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': i18n_languages_list,
            'FQMN': ['youtube', 'i18n_languages', 'list'],
        },
        'i18n_regions_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies the i18nRegion '
                            'resource properties that the API response will '
                            'include. Set the parameter value to snippet.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'hl',
                    'name': 'hl',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': i18n_regions_list,
            'FQMN': ['youtube', 'i18n_regions', 'list'],
        },
        'live_broadcasts_bind': {
            'help': 'Bind a broadcast to a stream.',
            'required_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'Broadcast to bind to the stream',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies a comma-separated '
                            'list of one or more liveBroadcast resource '
                            'properties that the API response will include. '
                            'The part names that you can include in the '
                            'parameter value are id, snippet, contentDetails, '
                            'and status.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'streamId',
                    'name': 'stream_id',
                    'type': 'string',
                    'help': 'Stream to bind, if not set unbind the current one.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': live_broadcasts_bind,
            'FQMN': ['youtube', 'live_broadcasts', 'bind'],
        },
        'live_broadcasts_delete': {
            'help': 'Delete a given broadcast.',
            'required_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'Broadcast to delete.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': live_broadcasts_delete,
            'FQMN': ['youtube', 'live_broadcasts', 'delete'],
        },
        'live_broadcasts_insert': {
            'help': 'Inserts a new stream for the authenticated user.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter serves two purposes in this '
                            'operation. It identifies the properties that the '
                            'write operation will set as well as the '
                            'properties that the API response will include. '
                            'The part properties that you can include in the '
                            'parameter value are id, snippet, contentDetails, '
                            'and status.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': live_broadcasts_insert,
            'FQMN': ['youtube', 'live_broadcasts', 'insert'],
        },
        'live_broadcasts_insert_cuepoint': {
            'help': 'Insert cuepoints in a broadcast',
            'required_params': [],
            'optional_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'Broadcast to insert ads to, or equivalently '
                            '`external_video_id` for internal use.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies a comma-separated '
                            'list of one or more liveBroadcast resource '
                            'properties that the API response will include. '
                            'The part names that you can include in the '
                            'parameter value are id, snippet, contentDetails, '
                            'and status.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'method': live_broadcasts_insert_cuepoint,
            'FQMN': ['youtube', 'live_broadcasts', 'insert_cuepoint'],
        },
        'live_broadcasts_list': {
            'help': 'Retrieve the list of broadcasts associated with the '
            'given channel.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies a comma-separated '
                            'list of one or more liveBroadcast resource '
                            'properties that the API response will include. '
                            'The part names that you can include in the '
                            'parameter value are id, snippet, contentDetails, '
                            'status and statistics.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'broadcastStatus',
                    'name': 'broadcast_status',
                    'type': 'string',
                    'help': 'Return broadcasts with a certain status, e.g. '
                            'active broadcasts.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'broadcastType',
                    'name': 'broadcast_type',
                    'type': 'string',
                    'help': 'Return only broadcasts with the selected type.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'Return broadcasts with the given ids from Stubby '
                            'or Apiary.',
                    'deprecated': False,
                    'repeated': True,
                },
                {
                    'originalName': 'maxResults',
                    'name': 'max_results',
                    'type': 'integer',
                    'help': 'The *maxResults* parameter specifies the maximum '
                            'number of items that should be returned in the '
                            'result set.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'mine',
                    'name': 'mine',
                    'type': 'boolean',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'pageToken',
                    'name': 'page_token',
                    'type': 'string',
                    'help': 'The *pageToken* parameter identifies a specific '
                            'page in the result set that should be returned. '
                            'In an API response, the nextPageToken and '
                            'prevPageToken properties identify other pages '
                            'that could be retrieved.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': live_broadcasts_list,
            'FQMN': ['youtube', 'live_broadcasts', 'list'],
        },
        'live_broadcasts_transition': {
            'help': 'Transition a broadcast to a given status.',
            'required_params': [
                {
                    'originalName': 'broadcastStatus',
                    'name': 'broadcast_status',
                    'type': 'string',
                    'help': 'The status to which the broadcast is going to '
                            'transition.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'Broadcast to transition.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies a comma-separated '
                            'list of one or more liveBroadcast resource '
                            'properties that the API response will include. '
                            'The part names that you can include in the '
                            'parameter value are id, snippet, contentDetails, '
                            'and status.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': live_broadcasts_transition,
            'FQMN': ['youtube', 'live_broadcasts', 'transition'],
        },
        'live_broadcasts_update': {
            'help': 'Updates an existing broadcast for the authenticated user.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter serves two purposes in this '
                            'operation. It identifies the properties that the '
                            'write operation will set as well as the '
                            'properties that the API response will include. '
                            'The part properties that you can include in the '
                            'parameter value are id, snippet, contentDetails, '
                            'and status. Note that this method will override '
                            'the existing values for all of the mutable '
                            'properties that are contained in any parts that '
                            'the parameter value specifies. For example, a '
                            "broadcast's privacy status is defined in the "
                            'status part. As such, if your request is '
                            'updating a private or unlisted broadcast, and '
                            "the request's part parameter value includes the "
                            "status part, the broadcast's privacy setting "
                            'will be updated to whatever value the request '
                            'body specifies. If the request body does not '
                            'specify a value, the existing privacy setting '
                            'will be removed and the broadcast will revert to '
                            'the default privacy setting.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': live_broadcasts_update,
            'FQMN': ['youtube', 'live_broadcasts', 'update'],
        },
        'live_chat_bans_delete': {
            'help': 'Deletes a chat ban.',
            'required_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [],
            'method': live_chat_bans_delete,
            'FQMN': ['youtube', 'live_chat_bans', 'delete'],
        },
        'live_chat_bans_insert': {
            'help': 'Inserts a new resource into this collection.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter serves two purposes in this '
                            'operation. It identifies the properties that the '
                            'write operation will set as well as the '
                            'properties that the API response returns. Set '
                            'the parameter value to snippet.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [],
            'method': live_chat_bans_insert,
            'FQMN': ['youtube', 'live_chat_bans', 'insert'],
        },
        'live_chat_messages_delete': {
            'help': 'Deletes a chat message.',
            'required_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [],
            'method': live_chat_messages_delete,
            'FQMN': ['youtube', 'live_chat_messages', 'delete'],
        },
        'live_chat_messages_insert': {
            'help': 'Inserts a new resource into this collection.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter serves two purposes. It '
                            'identifies the properties that the write '
                            'operation will set as well as the properties '
                            'that the API response will include. Set the '
                            'parameter value to snippet.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [],
            'method': live_chat_messages_insert,
            'FQMN': ['youtube', 'live_chat_messages', 'insert'],
        },
        'live_chat_messages_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [
                {
                    'originalName': 'liveChatId',
                    'name': 'live_chat_id',
                    'type': 'string',
                    'help': 'The id of the live chat for which comments '
                            'should be returned.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies the '
                            'liveChatComment resource parts that the API '
                            'response will include. Supported values are id, '
                            'snippet, and authorDetails.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'hl',
                    'name': 'hl',
                    'type': 'string',
                    'help': 'Specifies the localization language in which the '
                            'system messages should be returned.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'maxResults',
                    'name': 'max_results',
                    'type': 'integer',
                    'help': 'The *maxResults* parameter specifies the maximum '
                            'number of items that should be returned in the '
                            'result set. Not used in the streaming RPC.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'pageToken',
                    'name': 'page_token',
                    'type': 'string',
                    'help': 'The *pageToken* parameter identifies a specific '
                            'page in the result set that should be returned. '
                            'In an API response, the nextPageToken property '
                            'identify other pages that could be retrieved.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'profileImageSize',
                    'name': 'profile_image_size',
                    'type': 'integer',
                    'help': 'Specifies the size of the profile image that '
                            'should be returned for each user.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': live_chat_messages_list,
            'FQMN': ['youtube', 'live_chat_messages', 'list'],
        },
        'live_chat_messages_transition': {
            'help': 'Transition a durable chat event.',
            'required_params': [],
            'optional_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'The ID that uniquely identify the chat message '
                            'event to transition.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'status',
                    'name': 'status',
                    'type': 'string',
                    'help': 'The status to which the chat event is going to '
                            'transition.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': live_chat_messages_transition,
            'FQMN': ['youtube', 'live_chat_messages', 'transition'],
        },
        'live_chat_moderators_delete': {
            'help': 'Deletes a chat moderator.',
            'required_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [],
            'method': live_chat_moderators_delete,
            'FQMN': ['youtube', 'live_chat_moderators', 'delete'],
        },
        'live_chat_moderators_insert': {
            'help': 'Inserts a new resource into this collection.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter serves two purposes in this '
                            'operation. It identifies the properties that the '
                            'write operation will set as well as the '
                            'properties that the API response returns. Set '
                            'the parameter value to snippet.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [],
            'method': live_chat_moderators_insert,
            'FQMN': ['youtube', 'live_chat_moderators', 'insert'],
        },
        'live_chat_moderators_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [
                {
                    'originalName': 'liveChatId',
                    'name': 'live_chat_id',
                    'type': 'string',
                    'help': 'The id of the live chat for which moderators '
                            'should be returned.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies the '
                            'liveChatModerator resource parts that the API '
                            'response will include. Supported values are id '
                            'and snippet.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'maxResults',
                    'name': 'max_results',
                    'type': 'integer',
                    'help': 'The *maxResults* parameter specifies the maximum '
                            'number of items that should be returned in the '
                            'result set.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'pageToken',
                    'name': 'page_token',
                    'type': 'string',
                    'help': 'The *pageToken* parameter identifies a specific '
                            'page in the result set that should be returned. '
                            'In an API response, the nextPageToken and '
                            'prevPageToken properties identify other pages '
                            'that could be retrieved.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': live_chat_moderators_list,
            'FQMN': ['youtube', 'live_chat_moderators', 'list'],
        },
        'live_streams_delete': {
            'help': 'Deletes an existing stream for the authenticated user.',
            'required_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': live_streams_delete,
            'FQMN': ['youtube', 'live_streams', 'delete'],
        },
        'live_streams_insert': {
            'help': 'Inserts a new stream for the authenticated user.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter serves two purposes in this '
                            'operation. It identifies the properties that the '
                            'write operation will set as well as the '
                            'properties that the API response will include. '
                            'The part properties that you can include in the '
                            'parameter value are id, snippet, cdn, '
                            'content_details, and status.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': live_streams_insert,
            'FQMN': ['youtube', 'live_streams', 'insert'],
        },
        'live_streams_list': {
            'help': 'Retrieve the list of streams associated with the given '
            'channel. --',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies a comma-separated '
                            'list of one or more liveStream resource '
                            'properties that the API response will include. '
                            'The part names that you can include in the '
                            'parameter value are id, snippet, cdn, and status.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'Return LiveStreams with the given ids from '
                            'Stubby or Apiary.',
                    'deprecated': False,
                    'repeated': True,
                },
                {
                    'originalName': 'maxResults',
                    'name': 'max_results',
                    'type': 'integer',
                    'help': 'The *maxResults* parameter specifies the maximum '
                            'number of items that should be returned in the '
                            'result set.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'mine',
                    'name': 'mine',
                    'type': 'boolean',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'pageToken',
                    'name': 'page_token',
                    'type': 'string',
                    'help': 'The *pageToken* parameter identifies a specific '
                            'page in the result set that should be returned. '
                            'In an API response, the nextPageToken and '
                            'prevPageToken properties identify other pages '
                            'that could be retrieved.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': live_streams_list,
            'FQMN': ['youtube', 'live_streams', 'list'],
        },
        'live_streams_update': {
            'help': 'Updates an existing stream for the authenticated user.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter serves two purposes in this '
                            'operation. It identifies the properties that the '
                            'write operation will set as well as the '
                            'properties that the API response will include. '
                            'The part properties that you can include in the '
                            'parameter value are id, snippet, cdn, and '
                            'status. Note that this method will override the '
                            'existing values for all of the mutable '
                            'properties that are contained in any parts that '
                            'the parameter value specifies. If the request '
                            'body does not specify a value for a mutable '
                            'property, the existing value for that property '
                            'will be removed.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': live_streams_update,
            'FQMN': ['youtube', 'live_streams', 'update'],
        },
        'members_list': {
            'help': 'Retrieves a list of members that match the request '
            'criteria for a channel.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies the member '
                            'resource parts that the API response will '
                            'include. Set the parameter value to snippet.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'filterByMemberChannelId',
                    'name': 'filter_by_member_channel_id',
                    'type': 'string',
                    'help': 'Comma separated list of channel IDs. Only data '
                            'about members that are part of this list will be '
                            'included in the response.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'hasAccessToLevel',
                    'name': 'has_access_to_level',
                    'type': 'string',
                    'help': 'Filter members in the results set to the ones '
                            'that have access to a level.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'maxResults',
                    'name': 'max_results',
                    'type': 'integer',
                    'help': 'The *maxResults* parameter specifies the maximum '
                            'number of items that should be returned in the '
                            'result set.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'mode',
                    'name': 'mode',
                    'type': 'string',
                    'help': 'Parameter that specifies which channel members '
                            'to return.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'pageToken',
                    'name': 'page_token',
                    'type': 'string',
                    'help': 'The *pageToken* parameter identifies a specific '
                            'page in the result set that should be returned. '
                            'In an API response, the nextPageToken and '
                            'prevPageToken properties identify other pages '
                            'that could be retrieved.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': members_list,
            'FQMN': ['youtube', 'members', 'list'],
        },
        'memberships_levels_list': {
            'help': 'Retrieves a list of all pricing levels offered by a '
            'creator to the fans.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies the '
                            'membershipsLevel resource parts that the API '
                            'response will include. Supported values are id '
                            'and snippet.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [],
            'method': memberships_levels_list,
            'FQMN': ['youtube', 'memberships_levels', 'list'],
        },
        'playlist_images_delete': {
            'help': 'Deletes a resource.',
            'required_params': [],
            'optional_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'Id to identify this image. This is returned from '
                            'by the List method.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': playlist_images_delete,
            'FQMN': ['youtube', 'playlist_images', 'delete'],
        },
        'playlist_images_insert': {
            'help': 'Inserts a new resource into this collection.',
            'required_params': [],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies the properties '
                            'that the API response will include.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'method': playlist_images_insert,
            'FQMN': ['youtube', 'playlist_images', 'insert'],
        },
        'playlist_images_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [],
            'optional_params': [
                {
                    'originalName': 'maxResults',
                    'name': 'max_results',
                    'type': 'integer',
                    'help': 'The *maxResults* parameter specifies the maximum '
                            'number of items that should be returned in the '
                            'result set.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'pageToken',
                    'name': 'page_token',
                    'type': 'string',
                    'help': 'The *pageToken* parameter identifies a specific '
                            'page in the result set that should be returned. '
                            'In an API response, the nextPageToken and '
                            'prevPageToken properties identify other pages '
                            'that could be retrieved.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'parent',
                    'name': 'parent',
                    'type': 'string',
                    'help': 'Return PlaylistImages for this playlist id.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies a comma-separated '
                            'list of one or more playlistImage resource '
                            'properties that the API response will include. '
                            'If the parameter identifies a property that '
                            'contains child properties, the child properties '
                            'will be included in the response.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'method': playlist_images_list,
            'FQMN': ['youtube', 'playlist_images', 'list'],
        },
        'playlist_images_update': {
            'help': 'Updates an existing resource.',
            'required_params': [],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies the properties '
                            'that the API response will include.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'method': playlist_images_update,
            'FQMN': ['youtube', 'playlist_images', 'update'],
        },
        'playlist_items_delete': {
            'help': 'Deletes a resource.',
            'required_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': playlist_items_delete,
            'FQMN': ['youtube', 'playlist_items', 'delete'],
        },
        'playlist_items_insert': {
            'help': 'Inserts a new resource into this collection.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter serves two purposes in this '
                            'operation. It identifies the properties that the '
                            'write operation will set as well as the '
                            'properties that the API response will include.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': playlist_items_insert,
            'FQMN': ['youtube', 'playlist_items', 'insert'],
        },
        'playlist_items_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies a comma-separated '
                            'list of one or more playlistItem resource '
                            'properties that the API response will include. '
                            'If the parameter identifies a property that '
                            'contains child properties, the child properties '
                            'will be included in the response. For example, '
                            'in a playlistItem resource, the snippet property '
                            'contains numerous fields, including the title, '
                            'description, position, and resourceId '
                            'properties. As such, if you set *part=snippet*, '
                            'the API response will contain all of those '
                            'properties.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': True,
                },
                {
                    'originalName': 'maxResults',
                    'name': 'max_results',
                    'type': 'integer',
                    'help': 'The *maxResults* parameter specifies the maximum '
                            'number of items that should be returned in the '
                            'result set.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'pageToken',
                    'name': 'page_token',
                    'type': 'string',
                    'help': 'The *pageToken* parameter identifies a specific '
                            'page in the result set that should be returned. '
                            'In an API response, the nextPageToken and '
                            'prevPageToken properties identify other pages '
                            'that could be retrieved.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'playlistId',
                    'name': 'playlist_id',
                    'type': 'string',
                    'help': 'Return the playlist items within the given '
                            'playlist.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'videoId',
                    'name': 'video_id',
                    'type': 'string',
                    'help': 'Return the playlist items associated with the '
                            'given video ID.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': playlist_items_list,
            'FQMN': ['youtube', 'playlist_items', 'list'],
        },
        'playlist_items_update': {
            'help': 'Updates an existing resource.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter serves two purposes in this '
                            'operation. It identifies the properties that the '
                            'write operation will set as well as the '
                            'properties that the API response will include. '
                            'Note that this method will override the existing '
                            'values for all of the mutable properties that '
                            'are contained in any parts that the parameter '
                            'value specifies. For example, a playlist item '
                            'can specify a start time and end time, which '
                            'identify the times portion of the video that '
                            'should play when users watch the video in the '
                            'playlist. If your request is updating a playlist '
                            "item that sets these values, and the request's "
                            'part parameter value includes the contentDetails '
                            "part, the playlist item's start and end times "
                            'will be updated to whatever value the request '
                            'body specifies. If the request body does not '
                            'specify values, the existing start and end times '
                            'will be removed and replaced with the default '
                            'settings.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': playlist_items_update,
            'FQMN': ['youtube', 'playlist_items', 'update'],
        },
        'playlists_delete': {
            'help': 'Deletes a resource.',
            'required_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': playlists_delete,
            'FQMN': ['youtube', 'playlists', 'delete'],
        },
        'playlists_insert': {
            'help': 'Inserts a new resource into this collection.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter serves two purposes in this '
                            'operation. It identifies the properties that the '
                            'write operation will set as well as the '
                            'properties that the API response will include.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': playlists_insert,
            'FQMN': ['youtube', 'playlists', 'insert'],
        },
        'playlists_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies a comma-separated '
                            'list of one or more playlist resource properties '
                            'that the API response will include. If the '
                            'parameter identifies a property that contains '
                            'child properties, the child properties will be '
                            'included in the response. For example, in a '
                            'playlist resource, the snippet property contains '
                            'properties like author, title, description, '
                            'tags, and timeCreated. As such, if you set '
                            '*part=snippet*, the API response will contain '
                            'all of those properties.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'channelId',
                    'name': 'channel_id',
                    'type': 'string',
                    'help': 'Return the playlists owned by the specified '
                            'channel ID.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'hl',
                    'name': 'hl',
                    'type': 'string',
                    'help': 'Return content in specified language',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'Return the playlists with the given IDs for '
                            'Stubby or Apiary.',
                    'deprecated': False,
                    'repeated': True,
                },
                {
                    'originalName': 'maxResults',
                    'name': 'max_results',
                    'type': 'integer',
                    'help': 'The *maxResults* parameter specifies the maximum '
                            'number of items that should be returned in the '
                            'result set.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'mine',
                    'name': 'mine',
                    'type': 'boolean',
                    'help': 'Return the playlists owned by the authenticated '
                            'user.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'pageToken',
                    'name': 'page_token',
                    'type': 'string',
                    'help': 'The *pageToken* parameter identifies a specific '
                            'page in the result set that should be returned. '
                            'In an API response, the nextPageToken and '
                            'prevPageToken properties identify other pages '
                            'that could be retrieved.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': playlists_list,
            'FQMN': ['youtube', 'playlists', 'list'],
        },
        'playlists_update': {
            'help': 'Updates an existing resource.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter serves two purposes in this '
                            'operation. It identifies the properties that the '
                            'write operation will set as well as the '
                            'properties that the API response will include. '
                            'Note that this method will override the existing '
                            'values for mutable properties that are contained '
                            'in any parts that the request body specifies. '
                            "For example, a playlist's description is "
                            'contained in the snippet part, which must be '
                            'included in the request body. If the request '
                            'does not specify a value for the '
                            "snippet.description property, the playlist's "
                            'existing description will be deleted.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': playlists_update,
            'FQMN': ['youtube', 'playlists', 'update'],
        },
        'search_list': {
            'help': 'Retrieves a list of search resources',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies a comma-separated '
                            'list of one or more search resource properties '
                            'that the API response will include. Set the '
                            'parameter value to snippet.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'channelId',
                    'name': 'channel_id',
                    'type': 'string',
                    'help': 'Filter on resources belonging to this channelId.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'channelType',
                    'name': 'channel_type',
                    'type': 'string',
                    'help': 'Add a filter on the channel search.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'eventType',
                    'name': 'event_type',
                    'type': 'string',
                    'help': 'Filter on the livestream status of the videos.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'forContentOwner',
                    'name': 'for_content_owner',
                    'type': 'boolean',
                    'help': 'Search owned by a content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'forDeveloper',
                    'name': 'for_developer',
                    'type': 'boolean',
                    'help': 'Restrict the search to only retrieve videos '
                            'uploaded using the project id of the '
                            'authenticated user.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'forMine',
                    'name': 'for_mine',
                    'type': 'boolean',
                    'help': 'Search for the private videos of the '
                            'authenticated user.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'location',
                    'name': 'location',
                    'type': 'string',
                    'help': 'Filter on location of the video',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'locationRadius',
                    'name': 'location_radius',
                    'type': 'string',
                    'help': 'Filter on distance from the location (specified '
                            'above).',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'maxResults',
                    'name': 'max_results',
                    'type': 'integer',
                    'help': 'The *maxResults* parameter specifies the maximum '
                            'number of items that should be returned in the '
                            'result set.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'order',
                    'name': 'order',
                    'type': 'string',
                    'help': 'Sort order of the results.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'pageToken',
                    'name': 'page_token',
                    'type': 'string',
                    'help': 'The *pageToken* parameter identifies a specific '
                            'page in the result set that should be returned. '
                            'In an API response, the nextPageToken and '
                            'prevPageToken properties identify other pages '
                            'that could be retrieved.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'publishedAfter',
                    'name': 'published_after',
                    'type': 'string',
                    'help': 'Filter on resources published after this date.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'publishedBefore',
                    'name': 'published_before',
                    'type': 'string',
                    'help': 'Filter on resources published before this date.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'q',
                    'name': 'q',
                    'type': 'string',
                    'help': 'Textual search terms to match.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'regionCode',
                    'name': 'region_code',
                    'type': 'string',
                    'help': 'Display the content as seen by viewers in this '
                            'country.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'relevanceLanguage',
                    'name': 'relevance_language',
                    'type': 'string',
                    'help': 'Return results relevant to this language.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'safeSearch',
                    'name': 'safe_search',
                    'type': 'string',
                    'help': 'Indicates whether the search results should '
                            'include restricted content as well as standard '
                            'content.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'topicId',
                    'name': 'topic_id',
                    'type': 'string',
                    'help': 'Restrict results to a particular topic.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'type',
                    'name': 'type_',
                    'type': 'string',
                    'help': 'Restrict results to a particular set of resource '
                            'types from One Platform.',
                    'deprecated': False,
                    'repeated': True,
                },
                {
                    'originalName': 'videoCaption',
                    'name': 'video_caption',
                    'type': 'string',
                    'help': 'Filter on the presence of captions on the videos.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'videoCategoryId',
                    'name': 'video_category_id',
                    'type': 'string',
                    'help': 'Filter on videos in a specific category.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'videoDefinition',
                    'name': 'video_definition',
                    'type': 'string',
                    'help': 'Filter on the definition of the videos.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'videoDimension',
                    'name': 'video_dimension',
                    'type': 'string',
                    'help': 'Filter on 3d videos.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'videoDuration',
                    'name': 'video_duration',
                    'type': 'string',
                    'help': 'Filter on the duration of the videos.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'videoEmbeddable',
                    'name': 'video_embeddable',
                    'type': 'string',
                    'help': 'Filter on embeddable videos.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'videoLicense',
                    'name': 'video_license',
                    'type': 'string',
                    'help': 'Filter on the license of the videos.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'videoPaidProductPlacement',
                    'name': 'video_paid_product_placement',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'videoSyndicated',
                    'name': 'video_syndicated',
                    'type': 'string',
                    'help': 'Filter on syndicated videos.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'videoType',
                    'name': 'video_type',
                    'type': 'string',
                    'help': 'Filter on videos of a specific type.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': search_list,
            'FQMN': ['youtube', 'search', 'list'],
        },
        'subscriptions_delete': {
            'help': 'Deletes a resource.',
            'required_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [],
            'method': subscriptions_delete,
            'FQMN': ['youtube', 'subscriptions', 'delete'],
        },
        'subscriptions_insert': {
            'help': 'Inserts a new resource into this collection.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter serves two purposes in this '
                            'operation. It identifies the properties that the '
                            'write operation will set as well as the '
                            'properties that the API response will include.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [],
            'method': subscriptions_insert,
            'FQMN': ['youtube', 'subscriptions', 'insert'],
        },
        'subscriptions_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies a comma-separated '
                            'list of one or more subscription resource '
                            'properties that the API response will include. '
                            'If the parameter identifies a property that '
                            'contains child properties, the child properties '
                            'will be included in the response. For example, '
                            'in a subscription resource, the snippet property '
                            'contains other properties, such as a display '
                            'title for the subscription. If you set '
                            '*part=snippet*, the API response will also '
                            'contain all of those nested properties.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'channelId',
                    'name': 'channel_id',
                    'type': 'string',
                    'help': 'Return the subscriptions of the given channel '
                            'owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'forChannelId',
                    'name': 'for_channel_id',
                    'type': 'string',
                    'help': 'Return the subscriptions to the subset of these '
                            'channels that the authenticated user is '
                            'subscribed to.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'Return the subscriptions with the given IDs for '
                            'Stubby or Apiary.',
                    'deprecated': False,
                    'repeated': True,
                },
                {
                    'originalName': 'maxResults',
                    'name': 'max_results',
                    'type': 'integer',
                    'help': 'The *maxResults* parameter specifies the maximum '
                            'number of items that should be returned in the '
                            'result set.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'mine',
                    'name': 'mine',
                    'type': 'boolean',
                    'help': 'Flag for returning the subscriptions of the '
                            'authenticated user.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'myRecentSubscribers',
                    'name': 'my_recent_subscribers',
                    'type': 'boolean',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'mySubscribers',
                    'name': 'my_subscribers',
                    'type': 'boolean',
                    'help': 'Return the subscribers of the given channel owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'order',
                    'name': 'order',
                    'type': 'string',
                    'help': 'The order of the returned subscriptions',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'pageToken',
                    'name': 'page_token',
                    'type': 'string',
                    'help': 'The *pageToken* parameter identifies a specific '
                            'page in the result set that should be returned. '
                            'In an API response, the nextPageToken and '
                            'prevPageToken properties identify other pages '
                            'that could be retrieved.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': subscriptions_list,
            'FQMN': ['youtube', 'subscriptions', 'list'],
        },
        'super_chat_events_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies the '
                            'superChatEvent resource parts that the API '
                            'response will include. This parameter is '
                            'currently not supported.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'hl',
                    'name': 'hl',
                    'type': 'string',
                    'help': 'Return rendered funding amounts in specified '
                            'language.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'maxResults',
                    'name': 'max_results',
                    'type': 'integer',
                    'help': 'The *maxResults* parameter specifies the maximum '
                            'number of items that should be returned in the '
                            'result set.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'pageToken',
                    'name': 'page_token',
                    'type': 'string',
                    'help': 'The *pageToken* parameter identifies a specific '
                            'page in the result set that should be returned. '
                            'In an API response, the nextPageToken and '
                            'prevPageToken properties identify other pages '
                            'that could be retrieved.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': super_chat_events_list,
            'FQMN': ['youtube', 'super_chat_events', 'list'],
        },
        'tests_insert': {
            'help': 'POST method.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'externalChannelId',
                    'name': 'external_channel_id',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': tests_insert,
            'FQMN': ['youtube', 'tests', 'insert'],
        },
        'third_party_links_delete': {
            'help': 'Deletes a resource.',
            'required_params': [
                {
                    'originalName': 'linkingToken',
                    'name': 'linking_token',
                    'type': 'string',
                    'help': 'Delete the partner links with the given linking '
                            'token.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'type',
                    'name': 'type_',
                    'type': 'string',
                    'help': 'Type of the link to be deleted.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'externalChannelId',
                    'name': 'external_channel_id',
                    'type': 'string',
                    'help': 'Channel ID to which changes should be applied, '
                            'for delegation.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'Do not use. Required for compatibility.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'method': third_party_links_delete,
            'FQMN': ['youtube', 'third_party_links', 'delete'],
        },
        'third_party_links_insert': {
            'help': 'Inserts a new resource into this collection.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies the '
                            'thirdPartyLink resource parts that the API '
                            'request and response will include. Supported '
                            'values are linkingToken, status, and snippet.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'externalChannelId',
                    'name': 'external_channel_id',
                    'type': 'string',
                    'help': 'Channel ID to which changes should be applied, '
                            'for delegation.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': third_party_links_insert,
            'FQMN': ['youtube', 'third_party_links', 'insert'],
        },
        'third_party_links_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies the '
                            'thirdPartyLink resource parts that the API '
                            'response will include. Supported values are '
                            'linkingToken, status, and snippet.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'externalChannelId',
                    'name': 'external_channel_id',
                    'type': 'string',
                    'help': 'Channel ID to which changes should be applied, '
                            'for delegation.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'linkingToken',
                    'name': 'linking_token',
                    'type': 'string',
                    'help': 'Get a third party link with the given linking '
                            'token.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'type',
                    'name': 'type_',
                    'type': 'string',
                    'help': 'Get a third party link of the given type.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': third_party_links_list,
            'FQMN': ['youtube', 'third_party_links', 'list'],
        },
        'third_party_links_update': {
            'help': 'Updates an existing resource.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies the '
                            'thirdPartyLink resource parts that the API '
                            'request and response will include. Supported '
                            'values are linkingToken, status, and snippet.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'externalChannelId',
                    'name': 'external_channel_id',
                    'type': 'string',
                    'help': 'Channel ID to which changes should be applied, '
                            'for delegation.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': third_party_links_update,
            'FQMN': ['youtube', 'third_party_links', 'update'],
        },
        'thumbnails_set': {
            'help': 'As this is not an insert in a strict sense (it supports '
            'uploading/setting of a thumbnail for multiple videos, which '
            "doesn't result in creation of a single resource), I use a custom "
            'verb here.',
            'required_params': [
                {
                    'originalName': 'videoId',
                    'name': 'video_id',
                    'type': 'string',
                    'help': 'Returns the Thumbnail with the given video IDs '
                            'for Stubby or Apiary.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The '
                            'actual CMS account that the user authenticates '
                            'with must be linked to the specified YouTube '
                            'content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': thumbnails_set,
            'FQMN': ['youtube', 'thumbnails', 'set'],
        },
        'video_abuse_report_reasons_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies the videoCategory '
                            'resource parts that the API response will '
                            'include. Supported values are id and snippet.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'hl',
                    'name': 'hl',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': video_abuse_report_reasons_list,
            'FQMN': ['youtube', 'video_abuse_report_reasons', 'list'],
        },
        'video_categories_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies the videoCategory '
                            'resource properties that the API response will '
                            'include. Set the parameter value to snippet.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'hl',
                    'name': 'hl',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'Returns the video categories with the given IDs '
                            'for Stubby or Apiary.',
                    'deprecated': False,
                    'repeated': True,
                },
                {
                    'originalName': 'regionCode',
                    'name': 'region_code',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': video_categories_list,
            'FQMN': ['youtube', 'video_categories', 'list'],
        },
        'video_trainability_get': {
            'help': 'Returns the trainability status of a video.',
            'required_params': [],
            'optional_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'The ID of the video to retrieve.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': video_trainability_get,
            'FQMN': ['youtube', 'video_trainability', 'get'],
        },
        'videos_delete': {
            'help': 'Deletes a resource.',
            'required_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The '
                            'actual CMS account that the user authenticates '
                            'with must be linked to the specified YouTube '
                            'content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': videos_delete,
            'FQMN': ['youtube', 'videos', 'delete'],
        },
        'videos_get_rating': {
            'help': 'Retrieves the ratings that the authorized user gave to a '
            'list of specified videos.',
            'required_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': videos_get_rating,
            'FQMN': ['youtube', 'videos', 'get_rating'],
        },
        'videos_insert': {
            'help': 'Inserts a new resource into this collection.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter serves two purposes in this '
                            'operation. It identifies the properties that the '
                            'write operation will set as well as the '
                            'properties that the API response will include. '
                            'Note that not all parts contain properties that '
                            'can be set when inserting or updating a video. '
                            'For example, the statistics object encapsulates '
                            'statistics that YouTube calculates for a video '
                            'and does not contain values that you can set or '
                            'modify. If the parameter value specifies a part '
                            'that does not contain mutable values, that part '
                            'will still be included in the API response.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'autoLevels',
                    'name': 'auto_levels',
                    'type': 'boolean',
                    'help': 'Should auto-levels be applied to the upload.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'notifySubscribers',
                    'name': 'notify_subscribers',
                    'type': 'boolean',
                    'help': 'Notify the channel subscribers about the new '
                            'video. As default, the notification is enabled.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwnerChannel',
                    'name': 'on_behalf_of_content_owner_channel',
                    'type': 'string',
                    'help': 'This parameter can only be used in a properly '
                            'authorized request. *Note:* This parameter is '
                            'intended exclusively for YouTube content '
                            'partners. The *onBehalfOfContentOwnerChannel* '
                            'parameter specifies the YouTube channel ID of '
                            'the channel to which a video is being added. '
                            'This parameter is required when a request '
                            'specifies a value for the onBehalfOfContentOwner '
                            'parameter, and it can only be used in '
                            'conjunction with that parameter. In addition, '
                            'the request must be authorized using a CMS '
                            'account that is linked to the content owner that '
                            'the onBehalfOfContentOwner parameter specifies. '
                            'Finally, the channel that the '
                            'onBehalfOfContentOwnerChannel parameter value '
                            'specifies must be linked to the content owner '
                            'that the onBehalfOfContentOwner parameter '
                            'specifies. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and perform '
                            'actions on behalf of the channel specified in '
                            'the parameter value, without having to provide '
                            'authentication credentials for each separate '
                            'channel.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'stabilize',
                    'name': 'stabilize',
                    'type': 'boolean',
                    'help': 'Should stabilize be applied to the upload.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': videos_insert,
            'FQMN': ['youtube', 'videos', 'insert'],
        },
        'videos_list': {
            'help': 'Retrieves a list of resources, possibly filtered.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter specifies a comma-separated '
                            'list of one or more video resource properties '
                            'that the API response will include. If the '
                            'parameter identifies a property that contains '
                            'child properties, the child properties will be '
                            'included in the response. For example, in a '
                            'video resource, the snippet property contains '
                            'the channelId, title, description, tags, and '
                            'categoryId properties. As such, if you set '
                            '*part=snippet*, the API response will contain '
                            'all of those properties.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'chart',
                    'name': 'chart',
                    'type': 'string',
                    'help': 'Return the videos that are in the specified chart.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'hl',
                    'name': 'hl',
                    'type': 'string',
                    'help': 'Stands for "host language". Specifies the '
                            'localization language of the metadata to be '
                            'filled into snippet.localized. The field is '
                            'filled with the default metadata if there is no '
                            'localization in the specified language. The '
                            'parameter value must be a language code included '
                            'in the list returned by the i18nLanguages.list '
                            'method (e.g. en_US, es_MX).',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': 'Return videos with the given ids.',
                    'deprecated': False,
                    'repeated': True,
                },
                {
                    'originalName': 'locale',
                    'name': 'locale',
                    'type': 'string',
                    'help': None,
                    'deprecated': True,
                    'repeated': False,
                },
                {
                    'originalName': 'maxHeight',
                    'name': 'max_height',
                    'type': 'integer',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'maxResults',
                    'name': 'max_results',
                    'type': 'integer',
                    'help': 'The *maxResults* parameter specifies the maximum '
                            'number of items that should be returned in the '
                            'result set. *Note:* This parameter is supported '
                            'for use in conjunction with the myRating and '
                            'chart parameters, but it is not supported for '
                            'use in conjunction with the id parameter.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'maxWidth',
                    'name': 'max_width',
                    'type': 'integer',
                    'help': 'Return the player with maximum height specified in',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'myRating',
                    'name': 'my_rating',
                    'type': 'string',
                    'help': 'Return videos liked/disliked by the '
                            'authenticated user. Does not support '
                            'RateType.RATED_TYPE_NONE.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'pageToken',
                    'name': 'page_token',
                    'type': 'string',
                    'help': 'The *pageToken* parameter identifies a specific '
                            'page in the result set that should be returned. '
                            'In an API response, the nextPageToken and '
                            'prevPageToken properties identify other pages '
                            'that could be retrieved. *Note:* This parameter '
                            'is supported for use in conjunction with the '
                            'myRating and chart parameters, but it is not '
                            'supported for use in conjunction with the id '
                            'parameter.',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'regionCode',
                    'name': 'region_code',
                    'type': 'string',
                    'help': 'Use a chart that is specific to the specified '
                            'region',
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'videoCategoryId',
                    'name': 'video_category_id',
                    'type': 'string',
                    'help': 'Use chart that is specific to the specified '
                            'video category',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': videos_list,
            'FQMN': ['youtube', 'videos', 'list'],
        },
        'videos_rate': {
            'help': 'Adds a like or dislike rating to a video or removes a '
            'rating from a video.',
            'required_params': [
                {
                    'originalName': 'id',
                    'name': 'id_',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
                {
                    'originalName': 'rating',
                    'name': 'rating',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [],
            'method': videos_rate,
            'FQMN': ['youtube', 'videos', 'rate'],
        },
        'videos_report_abuse': {
            'help': 'Report abuse for a video.',
            'required_params': [],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': videos_report_abuse,
            'FQMN': ['youtube', 'videos', 'report_abuse'],
        },
        'videos_update': {
            'help': 'Updates an existing resource.',
            'required_params': [
                {
                    'originalName': 'part',
                    'name': 'part',
                    'type': 'string',
                    'help': 'The *part* parameter serves two purposes in this '
                            'operation. It identifies the properties that the '
                            'write operation will set as well as the '
                            'properties that the API response will include. '
                            'Note that this method will override the existing '
                            'values for all of the mutable properties that '
                            'are contained in any parts that the parameter '
                            "value specifies. For example, a video's privacy "
                            'setting is contained in the status part. As '
                            'such, if your request is updating a private '
                            "video, and the request's part parameter value "
                            "includes the status part, the video's privacy "
                            'setting will be updated to whatever value the '
                            'request body specifies. If the request body does '
                            'not specify a value, the existing privacy '
                            'setting will be removed and the video will '
                            'revert to the default privacy setting. In '
                            'addition, not all parts contain properties that '
                            'can be set when inserting or updating a video. '
                            'For example, the statistics object encapsulates '
                            'statistics that YouTube calculates for a video '
                            'and does not contain values that you can set or '
                            'modify. If the parameter value specifies a part '
                            'that does not contain mutable values, that part '
                            'will still be included in the API response.',
                    'deprecated': False,
                    'repeated': True,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The '
                            'actual CMS account that the user authenticates '
                            'with must be linked to the specified YouTube '
                            'content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': videos_update,
            'FQMN': ['youtube', 'videos', 'update'],
        },
        'watermarks_set': {
            'help': 'Allows upload of watermark image and setting it for a '
            'channel.',
            'required_params': [
                {
                    'originalName': 'channelId',
                    'name': 'channel_id',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': watermarks_set,
            'FQMN': ['youtube', 'watermarks', 'set'],
        },
        'watermarks_unset': {
            'help': 'Allows removal of channel watermark.',
            'required_params': [
                {
                    'originalName': 'channelId',
                    'name': 'channel_id',
                    'type': 'string',
                    'help': None,
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'optional_params': [
                {
                    'originalName': 'onBehalfOfContentOwner',
                    'name': 'on_behalf_of_content_owner',
                    'type': 'string',
                    'help': '*Note:* This parameter is intended exclusively '
                            'for YouTube content partners. The '
                            '*onBehalfOfContentOwner* parameter indicates '
                            "that the request's authorization credentials "
                            'identify a YouTube CMS user who is acting on '
                            'behalf of the content owner specified in the '
                            'parameter value. This parameter is intended for '
                            'YouTube content partners that own and manage '
                            'many different YouTube channels. It allows '
                            'content owners to authenticate once and get '
                            'access to all their video and channel data, '
                            'without having to provide authentication '
                            'credentials for each individual channel. The CMS '
                            'account that the user authenticates with must be '
                            'linked to the specified YouTube content owner.',
                    'deprecated': False,
                    'repeated': False,
                },
            ],
            'method': watermarks_unset,
            'FQMN': ['youtube', 'watermarks', 'unset'],
        },
    }
