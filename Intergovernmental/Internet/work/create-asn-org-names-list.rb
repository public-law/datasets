#!/usr/bin/env ruby


def get_org_name(asn)
  whois_data      = `whois #{asn}`.split("\n")
  org_name_record = whois_data.select{|r| r =~ /^OrgName:/}.first
  org_name        = org_name_record.split(':').last.strip
end

puts get_org_name('14593')
