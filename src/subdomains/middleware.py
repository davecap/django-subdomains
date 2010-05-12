import re
from django.conf import settings
from django.contrib.sites.models import Site

class SubdomainMiddleware(object):
    def process_request(self, request):
        """
        Adds a `subdomain` attribute to the request object, which corresponds
        to the portion of the URL before the current Site object's `domain` 
        attribute.
        """
        site = Site.objects.get_current()
        pattern = r'^(?:(?P<subdomain>.*?)\.)?%s:*$' % re.escape(site.domain)
        matches = re.match(pattern, request.get_host())
        
        request.subdomain = None
        
        if matches:
            request.subdomain = matches.group('subdomain')
        
        # Continue processing the request as normal.
        return None

class SubdomainURLRoutingMiddleware(SubdomainMiddleware):
    def process_request(self, request):
        """
        Sets the current request's `urlconf` attribute to the URL conf 
        associated with the subdomain, if listed in `SUBDOMAIN_URLCONFS`.
        """
        super(SubdomainURLRoutingMiddleware, self).process_request(request)
        
        subdomain = getattr(request, 'subdomain', False)
        
        if subdomain is not False:
            try:
                request.urlconf = settings.SUBDOMAIN_URLCONFS[subdomain]
            except KeyError:
                # There was no match in the SUBDOMAIN_URLCONFS setting, so let the
                # ROOT_URLCONF handle the URL routing for this request.
                pass
        
        # Continue processing the request as normal.
        return None